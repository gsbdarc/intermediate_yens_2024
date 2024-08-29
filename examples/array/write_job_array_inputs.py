# We specify the number of lines you want to generate with num_lines.
# We write a CSV file with two columns -- "Cashflows" and "Discount Rate"
# This file will be read by the job array with each task reading one line
import numpy as np
import csv

# specify the number of lines you want to generate
num_lines = 100

# Create and open a CSV file for writing
with open('inputs_to_job_array.csv', mode = 'w', newline = '') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE)

    # Generate and write num_lines lines of data
    for _ in range(num_lines):
        # first, output cashflows as a vector of length 100 with random cash flow over time periods
        outputs = list( np.random.uniform(-100, 100, 100))
        # second, append a random discount rate
        discount_rate = np.random.uniform(0.05, 0.15)
        outputs.append(discount_rate)
        csv_writer.writerow(outputs)

print(f'{num_lines} lines of data have been written to inputs_to_job_array.csv.')
