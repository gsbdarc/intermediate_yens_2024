---
title: 5. Command Line Arguments 
layout: page
nav_order: 5
parent: Day 4
updateDate: 2024-07-16
---

# {{ page.title }}

## Multiprocessing Script with Arguments
We can modify the parallel script to accept the number of cores as a command line argument.

We will use the value of `cpus-per-task` that we request from Slurm to pass it as an argument to the python script and use that value as the number of cores in parallel. That way we only need to set the `cpus-per-task` in `#SBATCH` line and use the value stored in the Slurm environment variable.

The modified [python script](https://github.com/gsbdarc/rf_bootcamp_2024/blob/main/examples/python_examples/3_investment-parallel-args.py), `3_investment-parallel-args.py`, accepts one argument, the number of cores to use for parallel `map` call. 

Look at the [slurm file](https://github.com/gsbdarc/rf_bootcamp_2024/blob/main/examples/python_examples/3_investment-parallel-args.slurm) called `3_investment-parallel-args.slurm` and edit it to include your email address.

Submit and monitor:
```bash
$ sbatch 3_investment-parallel-args.slurm 
```
