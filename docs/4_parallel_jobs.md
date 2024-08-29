---
title: 4. Parallel Script
layout: page
nav_order: 4
parent: Day 4
updateDate: 2024-07-16
---

# {{ page.title }}

## Multiprocessing Script
We can modify the `1_investment-serial.py` script to use `multiprocessing` python package to make the serial script parallel since all of the trials are independent.

{% include warning.html content="Because this Python code uses multiprocessing and the yens are a shared computing environment, we need to be careful about how Python sees and utilizes the shared cores on the yens."%}

Again, we will hard code the number of cores for
the script to use in this line in the python script:

```python
ncore = 12
````

Consider a slightly modified program, [2_investment-parallel.py](https://github.com/gsbdarc/rf_bootcamp_2024/blob/main/examples/python_examples/2_investment-parallel.py). 

**Important**: when using the yens, you must specify the number of cores in `Pool()` call. Otherwise, your python program would see all cores on the node and try to use them. But if you only request 10 cores in slurm and `Pool()` tries to use 256, bad things happen and your program will likely to get killed. Match the number of cores in the `Pool()` call to the number of cores you request in the submit script.

```python
# create a multiprocessing pool to run trials in parallel
pool = mp.Pool(processes = ncore)
```

We will have to adjust the [submit script](https://github.com/gsbdarc/rf_bootcamp_2024/blob/main/examples/python_examples/2_investment-parallel.slurm) as well to request more cores. We will request `cpus-per-task=12` (or using a shorthand `-c 12`) to request 12 cores to run in parallel.

Change the `2_investment-parallel.slurm` to include your email address.

To submit this script, we run:

```bash
$ sbatch 2_investment-parallel.slurm
```

Monitor the queue:

```bash
$ squeue
```

After the job has finished, look at the emails and output file. Compare the runtime of the serial and parallel script.
