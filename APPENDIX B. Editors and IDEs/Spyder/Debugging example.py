# Import Libraries
from rdkit import Chem
from rdkit.Chem import Descriptors

# A list of SMILES strings, one of which is invalid
smiles_list = [
    "CC(=O)OC1=CC=CC=C1C(=O)O",  # Aspirin (Valid)
    "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",  # Ibuprofen (Valid)
    "This is not a valid SMILES",  # Invalid SMILES string
    "CC(=O)NC1=CC=C(O)C=C1"  # Paracetamol (Valid)
]

results = []

#  Loop through the SMILES list to process each molecule
# Place a breakpoint on the line below (e.g., by pressing F12)
for smiles_string in smiles_list:
    mol = Chem.MolFromSmiles(smiles_string)
    # The script will fail here if you try to use 'mol' when it is None.
    # The debugger lets you inspect 'smiles_string' and 'mol' right before the error.
    if mol:
        mol_weight = Descriptors.MolWt(mol)
        results.append({"SMILES": smiles_string, "MolWt": mol_weight})
    else:
        results.append({"SMILES": smiles_string, "Error": "Invalid SMILES"})