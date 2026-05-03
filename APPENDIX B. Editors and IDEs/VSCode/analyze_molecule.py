from rdkit import Chem
from rdkit.Chem import Descriptors, Draw

# SMILES string for Aspirin (Acetylsalicylic Acid)
aspirin_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"

# Create a molecule object
mol = Chem.MolFromSmiles(aspirin_smiles)

if mol:
    # Calculate key descriptors
    mol_weight = Descriptors.MolWt(mol)
    log_p = Descriptors.MolLogP(mol)
    h_bond_donors = Descriptors.NumHDonors(mol)
    h_bond_acceptors = Descriptors.NumHAcceptors(mol)
    
    # Print the results
    print(f"Analysis for Aspirin:")
    print(f"  Molecular Weight: {mol_weight:.2f}")
    print(f"  LogP: {log_p:.2f}")
    print(f"  Hydrogen Bond Donors: {h_bond_donors}")
    print(f"  Hydrogen Bond Acceptors: {h_bond_acceptors}")
    
    # Generate and save an image of the molecule
    Draw.MolToFile(mol, 'aspirin.png')
    print("\nGenerated image of the molecule and saved to aspirin.png")
else:
    print("Error: Could not parse the SMILES string.")
    