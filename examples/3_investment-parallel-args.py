import time, sys
import numpy as np
import pandas as pd
import multiprocessing as mp
import matplotlib.pyplot as plt

np.errstate(over='ignore')

# accept command line arguments
# set the number of cores here from the command line. Avoid using mp.cpu_count() function on the yens.
ncore = int(sys.argv[1])

# define a function for NPV calculation
def npv_calculation(cashflows, discount_rate):
    # calculate NPV using the formula
    npv = np.sum(cashflows / (1 + discount_rate) ** np.arange(len(cashflows)))
    return npv

# function for simulating a single trial
def simulate_trial(trial_num):
    # randomly generate input values for each trial
    cashflows = np.random.uniform(-100, 100, 10000)  # Random cash flow vector over 10,000 time periods
    discount_rate = np.random.uniform(0.05, 0.15)  # Random discount rate

    # Ignore overflow warnings temporarily
    with np.errstate(over = 'ignore'):
        # calculate NPV for the trial
        npv = npv_calculation(cashflows, discount_rate)

    return npv

# number of trials
num_trials = 50000

start_time = time.time()

# create a multiprocessing pool to run trials in parallel
pool = mp.Pool(processes = ncore)

# perform the Monte Carlo simulation in parallel
results = pd.DataFrame( pool.map(simulate_trial, range(num_trials)), columns = ['NPV'] )

# close the pool and wait for all processes to finish
pool.close()
pool.join()

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")

print("Parallel NPV Calculation (using", ncore, "cores):")
# print summary statistics for NPV
print(results.describe())

# Plot a histogram of the results
plt.hist(results, bins=50, density=True, alpha=0.6, color='g')
plt.title('NPV distribution')
plt.xlabel('NPV Value')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
