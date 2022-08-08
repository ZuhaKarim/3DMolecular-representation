import numpy as np
from typing import Any, List
#from deepchem.utils.typing import RDKitMol
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import PyMol


smiles_array = []
smiles_20 = open('smiles_mol.out', 'r')
#smiles_20 = open('abc_mol.out', 'r')

for i in smiles_20:
    smiles_array.append(i[:-1])
print(smiles_array)


####
for i in smiles_array:
    v = PyMol.MolViewer()
    rdmol = Chem.MolFromSmiles(i)
    v.ShowMol(rdmol, name='mol')
    v.SaveFile('mol.pkl')
    cmd.bg_color('white')
    cmd.ray(600,600)
    cmd.set('ray_opaque_background', 0)
    cmd.png(" 2" +i +".png")

#  png ~/Desktop/test.png, width=10cm, dpi=300, ray=1

    #v.GetPNG()
