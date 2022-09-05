
import numpy as np
import pandas as pd
import pickle
from typing import Any, List
#from deepchem.utils.typing import RDKitMol
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import PyMol


#data_pik = pd.read_pickle("ConfGF_c1ccccc1.pkl")
with open('CGCF_QM9_6_OP.pkl', 'rb') as fp:
    Pickle_molecule_ = pickle.load(fp)
print(Pickle_molecule_)


v = PyMol.MolViewer()
#v.ShowMol(Pickle_molecule_, name='mol')
cmd.bg_color('white')
cmd.ray(600,600)
cmd.set('ray_opaque_background', 0)
#cmd.png(" pikle" +i +".png")

