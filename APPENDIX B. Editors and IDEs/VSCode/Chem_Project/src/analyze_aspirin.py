# File: src/analyze_aspirin.py

from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
import os

def main():
    """Analyzes aspirin and saves its 2D depiction to the project's output folder."""
    
    # Build a reliable path to the 'output' directory relative to this script's location.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, 'output')

    aspirin_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    mol = Chem.MolFromSmiles(aspirin_smiles)

    if mol:
        # Calculate and print properties
        print("Molecule: Aspirin")
        print(f"Molecular Weight: {Descriptors.MolWt(mol):.2f}")
        print(f"LogP: {Descriptors.MolLogP(mol):.2f}")
        print(f"H-Bond Donors: {Descriptors.NumHDonors(mol)}")
        print(f"H-Bond Acceptors: {Descriptors.NumHAcceptors(mol)}")

        # Ensure the output directory exists, then draw and save the molecule image.
        os.makedirs(output_dir, exist_ok=True)
        img_path = os.path.join(output_dir, 'aspirin_depiction.png')
        Draw.MolToFile(mol, img_path)
        print(f"\nSaved depiction to: {img_path}")
    else:
        print("Error: Could not parse SMILES string.")

if __name__ == "__main__":
    main()