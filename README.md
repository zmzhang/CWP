# Cheminformatics with Python

[![Book Page](https://img.shields.io/badge/Elsevier-Book%20Page-blue.svg)](https://shop.elsevier.com/books/cheminformatics-with-python/zhang/978-0-443-29186-9)

Welcome to the official code repository for the book **Cheminformatics with Python**. 

## About the Book
*Cheminformatics with Python* provides a ground-up, practical introduction that helps readers make effective use of the software. Covering four main parts—programming, data, methods, and applications—the book provides a brief introduction to the Python language and related scientific computing, cheminformatics, machine learning, and deep learning packages. 

It presents a systematic study of the representation of instrumental data, including molecular structures and common chemical databases. The methods section covers analytical signal processing, multivariate calibration, multivariate resolution, classical machine learning, and deep learning methods. Finally, the application section presents case studies of successful applications of cheminformatics in analytical chemistry, metabolomics, drug discovery, and materials science.

**Authors:** Hongmei Lu, Zhimin Zhang, Ming Wen  
**Publisher:** Elsevier  

## Repository Structure

The repository is organized chapter-by-chapter, containing Jupyter Notebooks, datasets, and script files accompanying the text:

- [**02. Python Basic**](<02. Python Basic/Chapter 02. Python Basics.ipynb>): Python basics and fundamentals.
- [**03. Python Packages**](<03. Python Packages/Chapter 03. Python Packages.ipynb>): Essential packages for scientific computing and cheminformatics.
- [**04. Representation of instrumental signals**](<04. Representation of instrumental signals/Chapter 04. Representation of instrumental signals.ipynb>): Matrix and sparse data representation.
- [**05. Representation of molecules**](<05. Representation of molecules/Chapter 05. Representation of molecules.ipynb>): Handling and processing molecular structure data.
- [**06. Databases in Chemistry**](<06. Databases in Chemistry/Chapter 06. Databases in Chemistry.ipynb>): Common chemical databases and access methods.
- [**07. Instrumental signal processing**](<07. Instrumental signal processing/Chapter 07. Instrumental signal processing.ipynb>): Signal processing workflows and smoothing techniques.
- [**08. Multivariate calibration and resolution**](<08. Multivariate calibration and resolution/Chapter 08. Multivariate calibration and resolution.ipynb>): Datasets and methods for calibration.
- [**09. Manipulation of molecular structures**](<09. Manipulation of molecular structures/Chapter 09. Manipulation of molecular structures.ipynb>): Modifying and analyzing molecular structures.
- [**10. Classic machine learning methods**](<10. Classic machine learning methods/Chapter 10. Classic machine learning methods.ipynb>): Traditional ML algorithms applied to cheminformatics.
- [**11. Deep learning methods**](<11. Deep learning methods/>): Deep learning architectures and applications in chemistry (contains multiple notebooks).
- [**12. Cheminformatics in Analytical Chemistry**](<12. Cheminformatics in Analytical Chemistry/Chapter 12. Cheminformatics in Analytical Chemistry.ipynb>): Case studies and workflows for analytical chemistry.
- [**13. Cheminformatics in Metabolomics**](<13. Cheminformatics in Metabolomics/Chapter 13. Cheminformatics in Metabolomics.ipynb>): Applications within metabolomics research.
- [**14. Cheminformatics in Drug Discovery**](<14. Cheminformatics in Drug Discovery/>): Workflows and ML for drug discovery (contains multiple notebooks).
- [**15. Cheminformatics in Materials Science**](<15. Cheminformatics in Materials Science/Chapter 15. Cheminformatics in Materials Science.ipynb>): Material science informatics applications.
- [**APPENDIX A**](<APPENDIX A. Necessary knowledge of Mathematics/APPENDIX A.ipynb>): Required mathematical, statistical, and information theory-related theories.
- [**APPENDIX B**](<APPENDIX B. Editors and IDEs/VSCode/>): Practical tips such as code editors.

## Getting Started

1. **Set up the environment:**
   We recommend using a virtual environment (such as  `venv`) to manage the core Python packages required for the notebooks. 
   
   Using `venv`:
   ```bash
   # Create a new virtual environment
   python -m venv cwp_env
   
   # Activate the environment (Windows)
   .\cwp_env\Scripts\activate
   # OR for macOS/Linux: source cwp_env/bin/activate
   
   # Install essential cheminformatics and data science libraries
   pip install rdkit jupyterlab numpy pandas scikit-learn
   ```

2. **Running the Notebooks:**
   Launch Jupyter Notebook, Jupyter Lab, or start the notebooks in VS Code in the root directory. Navigate to the individual chapter folders to explore and execute the `.ipynb` files.

## License
Please refer to the `LICENSE` file for details regarding the usage rights of the code.
