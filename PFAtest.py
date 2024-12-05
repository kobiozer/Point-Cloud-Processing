import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the data
file_path = "input.csv"
data = pd.read_csv(file_path)

# Assume you are using the 'Probability of False Alarm' column from the data
pfa_values = data['Probability of False Alarm'].values

# Find all values less than 1
values_below_1 = pfa_values[pfa_values < 1]

# Find the highest value below 1
highest_value_below_1 = np.max(values_below_1)

print(f"The highest value below 1 is: {highest_value_below_1}")
