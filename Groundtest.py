import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading data from the file
file_path = "input.csv"
data = pd.read_csv(file_path)

# Assuming the column with the values is 'z'
z_values = data['z']

# Calculating central statistics for the z values
mean_z = np.mean(z_values)
median_z = np.median(z_values)
std_z = np.std(z_values)
min_z = np.min(z_values)
max_z = np.max(z_values)

# Printing the central statistics
print(f"Mean Z: {mean_z}")
print(f"Median Z: {median_z}")
print(f"Standard Deviation of Z: {std_z}")
print(f"Min Z: {min_z}")
print(f"Max Z: {max_z}")

# Finding the highest value above 0, for example, 1
highest_value_above_0 = z_values[z_values >0].min()
print(f"The highest value below 1 is: {highest_value_above_0}")

# Analyzing if there are values between 0.1 and 0.2
values_between_01_and_02 = z_values[(z_values > 0.1) & (z_values < 1)]
print(f"Values between 0.1 and 1: {values_between_01_and_02}")

# Displaying a histogram for the distribution of z values
plt.hist(z_values, bins=50, color='blue', alpha=0.7)
plt.title('Distribution of Z values')
plt.xlabel('Z values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
