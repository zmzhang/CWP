# Import Libraries
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

#  Define a list of molecules (SMILES) and create a DataFrame
molecules_data = {
    "Name": ["Aspirin", "Ibuprofen", "Paracetamol"],
    "SMILES": [
        "CC(=O)OC1=CC=CC=C1C(=O)O",
        "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
        "CC(=O)NC1=CC=C(O)C=C1"
    ]
}
df = pd.DataFrame(molecules_data)

#  Calculate descriptors for each molecule
mols = [Chem.MolFromSmiles(smi) for smi in df['SMILES']]
df['Molecule_Object'] = mols
df['Molecular_Weight'] = [Descriptors.MolWt(m) for m in mols]
df['LogP'] = [Descriptors.MolLogP(m) for m in mols]