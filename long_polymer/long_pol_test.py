import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem

from pysoftk.linear_polymer.linear_polymer import *
from pysoftk.format_printers.format_mol import *
from pysoftk.topologies.diblock import *

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
    ptb7=Chem.MolFromMolFile(str(monomer_file))
    mol=Lp(ptb7,"Br", int(repetitions), shift=1.5).linear_polymer("MMFF", 100)
    AllChem.MMFFOptimizeMolecule(mol, nonBondedThresh=0.0001, maxIters=10000)
    Fmt(mol).pdb_print("chain_{}.pdb".format(repetitions))
    print ("Success")

if __name__ == "__main__":
    # Long polymers using unit polymer. This is good up to 20 units. Then it hangs due to extension of the polymer.
    #length_pol("unit.mol", 20)

    #This is using a new unit with 5 unit and repeating. It is useful up to 4 repetitions in my PC.
    length_pol("unit_5.mol", 1)
