---
title: 6. Job Arrays
layout: page
nav_order: 6
updateDate: 2024-08-29
---

# {{ page.title }}

One of Slurm's notable features is its ability to manage job arrays.

A Slurm job array is a convenient and efficient way to submit and manage a group of related jobs as a single entity. Instead of submitting each job individually, you can use <a href="https://slurm.schedmd.com/job_array.html" target="_blank">job arrays</a> to submit multiple similar tasks with a single command, making it easier to handle large-scale computations and parallel processing.

In this section, we will explore the concept of Slurm job arrays and  demonstrate how to leverage this feature for batch job processing, simplifying the management of repetitive tasks and improving overall productivity on the Yen environment.

Let's take a look at a [python script](https://github.com/gsbdarc/intermediate_yens_2024/blob/main/examples/array/4_investment-job-task.py), `4_investment-job-task.py`, that will be run as an array of tasks.

The script expects two command line arguments - cashflows and a discount rate and outputs NPV value for those inputs. Alternatively to using `multiprocessing` and `map()` function in `2_investment-parallel.py` script, we can compute NPV values over different inputs to the script that only computes the NPV value for 2 given inputs (cashflows and a discount rate). 

A job array is a common scheme for parameter sweep tasks. Each job array task will run the same script but with different inputs. 

To prepare inputs, we first run `write_job_array_inputs.py` script to write 100 lines of cashflows and discount rates that will be passed as inputs to `4_investment-job-task.py` script later. Each line corresponds to inputs for one job array task. 

```bash
# Activate venv if not activated yet
$ source venv/bin/activate

# Navigate to array subdirectory
$ cd array

# Make out directory for output files
$ mkdir out

# Run helper script to generate 100 inputs for job array
$ python write_job_array_inputs.py
```

You should see the following output:
```bash
100 lines of data have been written to inputs_to_job_array.csv.
```

Next, we'll submit a [job array script](https://github.com/gsbdarc/intermediate_yens_2024/blob/main/examples/array/4_investment-job-array.slurm), called `4_investment-job-array.slurm`, that runs 100 tasks in parallel using one line from input file to pass the value of arguments to the script.

This script extracts the line number that corresponds to the value of `$SLURM_ARRAY_TASK_ID` environment variable -- in this case, 1 through 100. When we submit this one slurm script to the scheduler, it will become 100 jobs running all at once with each task executing the `4_investment-job-task.py` script with different inputs. 

Another advantage of job arrays instead of running one big script is that if some but not all job tasks have failed, you can resubmit only those by using the failed array indices. For example, if the inputs for job task 50 produced NaN and job failed, we can fix the inputs, then resubmit the slurm script with `--array=50-50` to rerun only that task.

To submit the script that executes 100 jobs, run:

```bash
$ sbatch 4_investment-job-array.slurm 
```

You should then see 100 jobs in the queue. 

Each job task produces an out file with a computed NPV value.


## Job Dependency
Another useful Slurm feature is job dependency, where you can specify to run one job *only* after the first job finished okay (without errors) to chain script executions that way. 
For example, we impose job dependency to combine all of the NPV results into one CSV file only *after* all of the tasks have finished (without errors).
After you submit the `4_investment-job-array.slurm` script, you will know the job array ID so you can then run:

```bash
$ srun --dependency=afterok:<array_job_id> ./combine_array_results.sh
```

Replace `<array_job_id>` with your job array ID. This command will ensure that all job array tasks have finished with OK status and then run the shell script to combine the results. 

## Why Use `srun`?
`srun` respects job dependencies and ensures that the script runs only after the specified conditions are met, which might not be as straightforward if the script is executed directly.

When you use `srun --dependency=afterok:<jobid> ./combine_array_results.sh`, Slurm will:

- Wait for the array job to complete successfully.
- Allocate resources for the new job.
- Execute `combine_array_results.sh` on a compute yen-slurm node.

