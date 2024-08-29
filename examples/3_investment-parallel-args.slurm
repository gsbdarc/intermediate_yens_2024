#!/bin/bash

# Example of running parallel python script in a batch mode passing a command line argument to the script

#SBATCH -J npv-par-args
#SBATCH -p normal
#SBATCH -c 12                            # CPU cores (up to 256 on normal partition)
#SBATCH -t 1:00:00
#SBATCH -o out/npv-par-args-%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@stanford.edu

# Activate venv 
source venv/bin/activate

# Run python script with the number of cores as a command line arg
python 3_investment-parallel-args.py ${SLURM_CPUS_PER_TASK}
