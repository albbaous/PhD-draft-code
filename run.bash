#!/bin/bash
#$ -N GeneAnalysisJob    # Job name
#$ -cwd                  # Use the current working directory
#$ -o output.log         # Redirect output to a log file
#$ -e error.log          # Redirect errors to a log file

# Activate the conda environment
source /mnt/iusers01/bk01/a87652ab/miniconda3/bin/activate practice_env  # Ensu$

# Check the currently activated environment
echo "Activated conda environment: $CONDA_DEFAULT_ENV"

# List installed packages to verify pandas installationconda list

# Run your Python script
python parse_snp.py
