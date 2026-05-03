# %% Imports and Molecule Definition
from rdkit import Chem
from rdkit.Chem import Descriptors

# %% Aspirin's SMILES string
smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"

# %% Create a molecule object from the SMILES string
aspirin_mol = Chem.MolFromSmiles(smiles)

# %% Calculate and Print Properties
if aspirin_mol:
    # Calculate Molecular Weight
    mol_weight = Descriptors.MolWt(aspirin_mol)
    
    # Calculate LogP
    log_p = Descriptors.MolLogP(aspirin_mol)
    
    print(f"Molecule: Aspirin")
    print(f"Molecular Weight: {mol_weight:.2f}")
    print(f"LogP: {log_p:.2f}")
else:
    print(f"Could not create molecule from SMILES: {smiles}")