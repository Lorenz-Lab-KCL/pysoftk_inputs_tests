import pytest
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdDistGeom

from pysoftk.topologies.diblock import *
from pysoftk.topologies.ring import *
from pysoftk.topologies.branched import *
from pysoftk.topologies.ranpol import *

from pysoftk.format_printers.format_mol import *
from pysoftk.folder_manager.folder_creator import *

from itertools import permutations
from pysoftk.linear_polymer.utils import *

alph1=permutations(["A", "B", "C", "D"], 4)
string=[''.join(values) for idx, values in enumerate(alph1)]

mols=[Chem.MolFromSmiles('c1cc(oc1Br)Br'),
      Chem.MolFromSmiles('c1cc(sc1Br)Br'),
      Chem.MolFromSmiles('c1(ccc(cc1)Br)Br'),
      Chem.MolFromSmiles('c1(ccc(nc1)Br)Br')]

#results=[]
#for idx, values in enumerate(string):
#    patt=Pt(values, mols, "Br").pattern_block_poly(swap_H=False)
#    Fmt(patt).xyz_print(values+".xyz")
#    #results.append((values,Chem.MolToSmiles(patt)))

patt=Pt(string[0], mols, "Br").pattern_block_poly(swap_H=False)

from pysoftk.linear_polymer.linear_polymer import *
from pysoftk.format_printers.format_mol import *

new=Lp(patt,"Br", 2, shift=1.0).linear_polymer("MMFF", 5)
Fmt(new).xyz_print("ABCD_pol.xyz")



   

