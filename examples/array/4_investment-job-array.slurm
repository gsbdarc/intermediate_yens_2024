#!/bin/bash

# Example of running python script as a job array

#SBATCH -J inv-array
#SBATCH --array=1-100
#SBATCH -p normal
#SBATCH -c 1                            # CPU cores per task (up to 256 on normal partition)
#SBATCH -t 10:00
#SBATCH -o out/inv-array-%a.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@stanford.edu

# Read in a specified line number from input file
# line number corresponds to job array task ID
export NUM=$SLURM_ARRAY_TASK_ID
export INPUTS=$(sed "${NUM}q;d" inputs_to_job_array.csv)

# Activate venv 
source ../venv/bin/activate

# Run every job array task in parallel
python 4_investment-job-task.py $INPUTS

