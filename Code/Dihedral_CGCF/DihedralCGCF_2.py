import pandas as pd
import pymol
from pymol import cmd
from glob import glob

# load all molecules
[cmd.load(x) for x in glob(f'./XYZ_CGCF/XYZ_Trial2/*.xyz')]

molecules = cmd.get_object_list('all')   ## equiv. to `molecules = ('molecule-1', 'molecule-2')`

conformation_list = []
dihed_list_1 = []
dihed_list_2 = []
dihed_list_3 = []
dihed_list_4 = []
dihed_list_5 = []
dihed_list_6 = []

print(f'Total number of molecules: {len(molecules)}')
for target in molecules:
    conformation_list.append(target)
    dihed_list_1.append(cmd.get_dihedral(f'{target} & id 1',
                                         f'{target} & id 2',
                                         f'{target} & id 3',
                                         f'{target} & id 4'))
    dihed_list_2.append(cmd.get_dihedral(f'{target} & id 2',
                                         f'{target} & id 3',
                                         f'{target} & id 4',
                                         f'{target} & id 5'))
    dihed_list_3.append(cmd.get_dihedral(f'{target} & id 3',
                                         f'{target} & id 4',
                                         f'{target} & id 5',
                                         f'{target} & id 6'))
    dihed_list_4.append(cmd.get_dihedral(f'{target} & id 4',
                                         f'{target} & id 5',
                                         f'{target} & id 6',
                                         f'{target} & id 7'))
    dihed_list_5.append(cmd.get_dihedral(f'{target} & id 5',
                                         f'{target} & id 6',
                                         f'{target} & id 7',
                                         f'{target} & id 8'))
    dihed_list_6.append(cmd.get_dihedral(f'{target} & id 6',
                                         f'{target} & id 7',
                                         f'{target} & id 8',
                                         f'{target} & id 9'))

torsion_df = pd.DataFrame(
    {'conformation': conformation_list,
     'torsion_1': dihed_list_1,
     'torsion_2': dihed_list_2,
     'torsion_3': dihed_list_3,
     'torsion_4': dihed_list_4,
     'torsion_5': dihed_list_5,
     'torsion_6': dihed_list_6
    })

torsion_df.to_csv("torsions_2.csv", index=False)

print('DONE')
