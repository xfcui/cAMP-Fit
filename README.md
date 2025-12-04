# cAMP Binding to GmCNGC30 Activates Channel Activity

## Overview
This project simulates the binding of **cAMP** to **GmCNGC30** and its effect on channel activation.  
The workflow performs **template-based docking**, linker conformer selection, and **energy minimization** using **AmberTools**.  
All results are automatically saved in the `result/` folder.

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

 Create and activate the environment:

    conda env create -f environment.yml
    conda activate AmberTools23




## Usage
To run the docking and minimization pipeline, execute the main script:

    cd code
    bash run.sh



