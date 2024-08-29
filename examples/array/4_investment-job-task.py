import sys, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.errstate(over='ignore')

# pick up cashflows and discount rate from command line
args = sys.argv[1] # this will be a long string that we need to convert into a cashflows vector of floats and discount rate as a float
args_list = args.split(',')

# Convert the list of strings to a list of floats
cashflows = [float(x) for x in args_list[:-1]]
discount_rate = float(args_list[-1])

# define a function for NPV calculation
def npv_calculation(cashflows, discount_rate):
    # ignore overflow warnings temporarily
    with np.errstate(over = 'ignore'):
        # calculate NPV using the formula
        npv = np.sum(cashflows / (1 + discount_rate) ** np.arange(len(cashflows)))
        return npv

results = npv_calculation(cashflows, discount_rate)
print(results)
