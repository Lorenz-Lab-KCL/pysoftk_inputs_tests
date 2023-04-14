import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdDistGeom

from pysoftk.topologies.diblock import *
from pysoftk.format_printers.format_mol import *
import itertools

import os
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        import time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print('Elapsed time for matrix calculation: {:.4f} seconds'.format(total_time))
        return result
    return timeit_wrapper

@timeit
def length_pol(monomer_file, repetitions):
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = list(itertools.chain.from_iterable(string))
    
    mols=[Chem.MolFromMolFile(str(monomer_file)) for _ in range(repetitions)]
    seq= [letter[i] for i in range(repetitions)]

    patt=Pt("".join(seq), mols, "Br").pattern_block_poly(relax_iterations=10000)
    Fmt(patt).pdb_print("chain_{}.pdb".format(repetitions))
    print ("Success")

if __name__ == "__main__":
    # Patterned polymers using unit polymer. This is good up to 20 units. Then it hangs due to extension of the polymer.
    length_pol("unit.mol", 2)
    
    # Patterned polymers using 5_unit polymer. This is good up to 20 units. Then it hangs due to extension of the polymer.
    #length_pol("unit_5.mol", 5)
