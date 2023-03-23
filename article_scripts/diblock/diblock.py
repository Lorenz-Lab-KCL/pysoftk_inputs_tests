from rdkit import Chem
from rdkit.Chem import AllChem

mol_1=Chem.MolFromSmiles('BrCOCBr')
mol_2=Chem.MolFromSmiles('[C@H](CBr)(OBr)C')

from pysoftk.format_printers.format_mol import *
from pysoftk.topologies.diblock import *

poly=Db(mol_1,mol_2,"Br").diblock_copolymer(5,7,"MMFF",10)
Fmt(poly).xyz_print("diblock.xyz")
