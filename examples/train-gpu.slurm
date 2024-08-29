#!/bin/bash

# Example slurm script to train pytorch DL model on Yen GPU

#SBATCH -J train-gpu
#SBATCH -p gpu
#SBATCH -c 10
#SBATCH -N 1
#SBATCH -t 1-             # limit of 1 day runtime
#SBATCH -G 1              # limit of 4 GPUs per user
#SBATCH -o out/train-gpu-%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@stanford.edu

# Load pytorch module 
ml pytorch

# Run training script on GPU
python mnist.py

