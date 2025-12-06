# cAMP Binding to GmCNGC30 Activates Channel Activity

## Overview
This project simulates the binding of **cAMP** to **GmCNGC30** and its effect on channel activation.  
The workflow performs **template-based docking**, linker conformer selection, and **energy minimization** using **AmberTools**.  
All results are automatically saved in the `result/` folder.

The key steps of this project—structure preparation, force-field parameter generation, and energy minimization—all rely on **AmberTools 23**.
For installation instructions and usage guidelines for AmberTools, please refer to the official documentation:
https://ambermd.org/AmberTools.php

---

## Directory Structure
The repository is organized as follows:

    project_root/
    ├── environment.yml        # Conda environment configuration
    ├── code/                  # Source code and execution scripts
    │   ├── run.sh             # Main execution script
    │   └── ...
    ├── data/                  # Input data and intermediate files
    │   └── ...
    ├── result/                # Output directory for final results
    └── README.md

---

## Environment Setup
Make sure you have **Conda** installed.

You can configure the entire environment for this project — including AmberTools 23 and all other dependencies — by running the following commands:

    conda env create -f environment.yml
    conda activate AmberTools23




## Usage
To run the template-based docking, linker conformer selection, and energy minimization pipeline, simply execute the main workflow script.
This script performs all steps automatically, including preparing input files, running AmberTools modules, and saving results to the `result/` directory.

    cd code
    bash run.sh

After the script finishes:

- All intermediate files will be stored in the `data/` folder.

- Final minimized complexes and docking outputs will appear in the `result/` folder.


