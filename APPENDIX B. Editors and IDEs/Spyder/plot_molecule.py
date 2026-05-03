# Import necessary libraries
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

# Create molecule and generate a 2D depiction
caffeine_mol = Chem.MolFromSmiles("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")  # Caffeine
img = Draw.MolToImage(caffeine_mol)

# Display the image using Matplotlib
plt.figure(figsize=(4, 4))
plt.imshow(img)
plt.title("2D Structure of Caffeine")
plt.axis('off')  # Hide the axes
plt.show()