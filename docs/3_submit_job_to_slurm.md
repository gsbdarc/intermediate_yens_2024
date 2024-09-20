---
title: 3. Submit Your First Job to Yen-Slurm
layout: page
nav_order: 3
updateDate: 2024-08-29
---

# {{ page.title }}


## Running Python Script on the Command Line 
Navigate to the `examples` directory. Just as we ran the R script on the interactive yen nodes, we can run the Python script on the command line.  

Let's run a python version of the script, `1_investment-serial.py`, which is a serial version of the script that does not use multiprocessing.  View the complete script [here](https://github.com/gsbdarc/intermediate_yens_2024/blob/main/examples/1_investment-serial.py).

Activate your virtual python environment, `venv`, first:

```
cd examples
source venv/bin/activate
```

Run the script like so: 
```bash
python 1_investment-serial.py
```

The output should look like:
```bash
Elapsed time: 12.10 seconds
Serial NPV Calculation:
                NPV
count  50000.000000
mean       0.091370
std      143.905996
min     -641.639860
25%      -95.829987
50%        0.081198
75%       96.030578
max      592.636589
```

## Submit Serial Script to the Scheduler

We'll prepare a submission [slurm script](https://github.com/gsbdarc/intermediate_yens_2024/blob/main/examples/1_investment-serial.slurm), called `1_investment-serial.slurm` and submit it to the scheduler. Edit the slurm script to include
your email address.

The important arguments here are that you request:
* `#SBATCH -p` is the partition you are submitting your job to 
* `#SBATCH -c` is the number of CPUs
* `#SBATCH -t` is the amount of time for your job
* `#SBATCH --mem` is the amount of total memory; if not included in the slurm script, get 4G of RAM per core requested on `normal` partition`


We are going to make an `out` directory for storing all the output files, then submit the script:

```bash
mkdir -p out
sbatch 1_investment-serial.slurm
```

You should see a similar output:

```bash
Submitted batch job 44097
```

Monitor your job:
```bash
squeue
```

- `JOBID` lists a unique numeric job ID for this job.
- `PARTITION` lists the partition the job is submitted to (`normal`, `dev`, `long` or `gpu`).
- `NAME` lists the job name that the user specified in the submission script (if no name is supplied,
the name of the submission batch script is used). Job names do not have to be unique.
- `USER` indicates the yen user who submitted the job.
- `ST` lists the job state. `R` means the job is running and `PD` means the job is pending in the queue.
- `TIME` lists the time the job has been running. Pending jobs will have time 0:00 until they start running.
- `NODES` lists how many different machines or nodes the job is running on (1 means the job is running on one node only and 2 means the job is running on two nodes, and so on).
- `NODELIST(REASON)` lists the hostname for the node that the job is running on (`yen11`, `yen12`, `yen13`, `yen14`, `yen15`, `yen16`, `yen17`, `yen18`, `yen-gpu1`, `yen-gpu2` or `yen-gpu3`).

{: .tip}
For pending jobs, you will see a reason why this jobs has not started yet. Common reasons are `(Resources)` when the job is waiting on resources
such as CPU cores, GPU's or memory to be available before it can start and `(Priority)` when the job is lower in priority than other jobs in the queue
but the resources are available.

Filtering this command for your user will display only your running and queued jobs:

```bash
squeue -u $USER
```


The script should take less than a minute to complete. Look at the slurm emails after the job is finished. Slurm email will summarize CPU and RAM utilization which you can use to adjust future runs if you are under-utilizing the requested resources. 

Since the job is executed in batch mode, you will not see anything printed to the screen. All print statements go into the specified output file. While the job is running, you can look at the output file with:

```bash
tail -f out/npv-serial*out
```

### How Do I Cancel My Job on Yen-Slurm?

The `scancel JOBID` command will cancel your job.  You can find the unique numeric `JOBID` of your job with `squeue`.
You can also cancel all of your running and pending jobs with `scancel -u USERNAME` where `USERNAME` is your username.

