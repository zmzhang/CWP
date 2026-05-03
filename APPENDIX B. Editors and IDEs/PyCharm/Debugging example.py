import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# A list of common painkillers
painkillers = {
    "Name": ["Aspirin", "Ibuprofen", "Paracetamol", "Naproxen"],
    "SMILES": [
        "CC(=O)OC1=CC=CC=C1C(=O)O",
        "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
        "CC(=O)NC1=CC=C(O)C=C1",
        "C1=CC(=CC=C1C(C)C(=O)O)OC"
    ]
}

df = pd.DataFrame(painkillers)

# Calculate properties using RDKit
mols = [Chem.MolFromSmiles(smi) for smi in df["SMILES"]]
df["MolWt"] = [Descriptors.MolWt(mol) for mol in mols]
df["LogP"] = [Descriptors.MolLogP(mol) for mol in mols]
df["NumRings"] = [Descriptors.RingCount(mol) for mol in mols]

# Set a breakpoint on the line below to inspect the 'df' DataFrame
print("DataFrame calculation complete. Debugger can inspect 'df'.")