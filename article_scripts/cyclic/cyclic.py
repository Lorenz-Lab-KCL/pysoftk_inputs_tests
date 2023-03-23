from rdkit import Chem
from rdkit.Chem import AllChem

from pysoftk.topologies.ring import *
from pysoftk.format_printers.format_mol import *

mol=Chem.MolFromSmiles("c1cc(ccc1Br)Br")
AllChem.EmbedMolecule(mol)
  
hom=Rn(mol,'Br').pol_ring(5,FF="UFF",iters=1000)
Fmt(hom).xyz_print("ring5.xyz")
