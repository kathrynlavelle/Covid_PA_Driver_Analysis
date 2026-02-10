# README

## Overview
This is a knowledge discovery project focused on answering the question, "Are Pennsylvanians driving worse post-COVID?"
The investigative analysis is based on PennDOT crash data from 2005 - 2024. The goal is to discover patterns and evidence-based insights to inform the general public about statistically-sigificant behavior or traffic safety trends. 


## Repository Structure
Covid_Driver_Analysis_Project/
│
├── README.md*        # This file contains the project file structure and navigation guide
├── requirements.txt  # Python packages used
│
├── data/           
│   ├── raw/                                # Original data files, downloaded by the `download-data.py` script
│   ├── processed/                          # Cleaned and engineered datasets
│   ├── Crash Database Primer 10-16.pdf     # Copy of the PennDOT Crash Database Primer
│   ├── Crash_Data_Dictionary_2025.pdf      # Copy of the PennDOT Crash Data Dictionary
│   └── CONTEXT.md                          # This file contains the context of the data
│
├── notebooks/                  # Analysis notebooks
│   ├── 01-exploration.ipynb    # Data exploration and understanding (EDA)
│   ├── 02-modeling.ipynb       # Data preparation and modeling
│
├── results/
│   ├── figures/    # Charts and visualizations 
│
├── src/                    # Python scripts
│   ├── download-data.py    # Script to download the data from the PennDOT website



## How to Run
Basic instructions for reproducing analysis in VS Code.

1. Open .ipynb files from /notebooks directory in VS Code
2. Setup an environment and install dependencies

    ## Setup and Dependencies
    How to recreate the environment in VS Code.

    1. Create a Conda environment
    2. Activate the new Conda environment
    3. Install dependencies from requirements.txt
        pip install -r requirements.txt
    4. Select the Interpreter in VS Code
        Command Palette > Python: Select Interpreter > Choose environment

3. Run notebook files (e.g. 01-explortion.ipynb)
Data loading may incur delay before any analysis or visualizations are generated.
