from rdkit import Chem
from rdkit.Chem import Descriptors
from typing import Optional, Tuple


def validate_smiles(smiles: str) -> Tuple[bool, Optional[str]]:
    """
    Validate a SMILES string and return validation status with error message if invalid.
    
    Args:
        smiles (str): The SMILES string to validate
        
    Returns:
        Tuple[bool, Optional[str]]: (is_valid, error_message)
            - is_valid: True if SMILES is valid, False otherwise
            - error_message: None if valid, error description if invalid
    """
    if not smiles or not isinstance(smiles, str):
        return False, "SMILES string cannot be empty or non-string"
    
    # Remove any whitespace
    smiles = smiles.strip()
    
    if not smiles:
        return False, "SMILES string cannot be empty after removing whitespace"
    
    try:
        # Attempt to parse the SMILES string
        mol = Chem.MolFromSmiles(smiles)
        
        if mol is None:
            return False, "Invalid SMILES string - could not parse molecular structure"
        
        # Additional validation: check if molecule has atoms
        if mol.GetNumAtoms() == 0:
            return False, "SMILES string represents an empty molecule"
        
        return True, None
        
    except Exception as e:
        return False, f"Error parsing SMILES string: {str(e)}"


def calculate_molecular_weight(smiles: str) -> Optional[float]:
    """
    Calculate the molecular weight of a molecule from its SMILES string.
    
    Args:
        smiles (str): The SMILES string of the molecule
        
    Returns:
        Optional[float]: Molecular weight in g/mol if valid SMILES, None if invalid
    """
    is_valid, error_msg = validate_smiles(smiles)
    
    if not is_valid:
        print(f"Error: {error_msg}")
        return None
    
    try:
        mol = Chem.MolFromSmiles(smiles.strip())
        molecular_weight = Descriptors.MolWt(mol)
        return molecular_weight
    
    except Exception as e:
        print(f"Error calculating molecular weight: {str(e)}")
        return None


def analyze_molecule(smiles: str) -> dict:
    """
    Comprehensive analysis of a molecule from its SMILES string.
    
    Args:
        smiles (str): The SMILES string of the molecule
        
    Returns:
        dict: Dictionary containing molecular properties or error information
    """
    # Validate SMILES first
    is_valid, error_msg = validate_smiles(smiles)
    
    if not is_valid:
        return {
            "valid": False,
            "error": error_msg,
            "smiles": smiles
        }
    
    try:
        mol = Chem.MolFromSmiles(smiles.strip())
        
        # Calculate various molecular descriptors
        properties = {
            "valid": True,
            "smiles": smiles.strip(),
            "molecular_weight": Descriptors.MolWt(mol),
            "logp": Descriptors.MolLogP(mol),
            "h_bond_donors": Descriptors.NumHDonors(mol),
            "h_bond_acceptors": Descriptors.NumHAcceptors(mol),
            "rotatable_bonds": Descriptors.NumRotatableBonds(mol),
            "aromatic_rings": Descriptors.NumAromaticRings(mol),
            "num_atoms": mol.GetNumAtoms(),
            "molecular_formula": Chem.rdMolDescriptors.CalcMolFormula(mol)
        }
        
        return properties
        
    except Exception as e:
        return {
            "valid": False,
            "error": f"Error analyzing molecule: {str(e)}",
            "smiles": smiles
        }


def main():
    """
    Example usage of the SMILES validation and molecular weight calculation functions.
    """
    # Test molecules with different complexities
    test_molecules = [
        ("CC(=O)OC1=CC=CC=C1C(=O)O", "Aspirin"),
        ("CCO", "Ethanol"),
        ("C1=CC=CC=C1", "Benzene"),
        ("CC(C)CC1=CC=C(C=C1)C(C)C(=O)O", "Ibuprofen"),
        ("invalid_smiles", "Invalid SMILES"),
        ("", "Empty string"),
        ("C", "Methane")
    ]
    
    print("SMILES Validation and Molecular Weight Analysis")
    print("=" * 50)
    
    for smiles, name in test_molecules:
        print(f"\nAnalyzing {name}:")
        print(f"SMILES: {smiles}")
        
        # Validate SMILES
        is_valid, error_msg = validate_smiles(smiles)
        print(f"Valid SMILES: {is_valid}")
        
        if is_valid:
            # Calculate molecular weight
            mol_weight = calculate_molecular_weight(smiles)
            if mol_weight:
                print(f"Molecular Weight: {mol_weight:.2f} g/mol")
                
            # Get comprehensive analysis
            analysis = analyze_molecule(smiles)
            if analysis["valid"]:
                print(f"Molecular Formula: {analysis['molecular_formula']}")
                print(f"LogP: {analysis['logp']:.2f}")
                print(f"H-bond Donors: {analysis['h_bond_donors']}")
                print(f"H-bond Acceptors: {analysis['h_bond_acceptors']}")
        else:
            print(f"Error: {error_msg}")


if __name__ == "__main__":
    main()