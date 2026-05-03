"""A module for performing various cheminformatics calculations.

This module provides functions for tasks such as calculating molecular weight
from SMILES strings.
"""

from rdkit import Chem
from rdkit.Chem import Descriptors

def calculate_mw(smiles: str) -> float:
    """Calculates the molecular weight for a given SMILES string."""
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return Descriptors.MolWt(mol)
    return 0.0