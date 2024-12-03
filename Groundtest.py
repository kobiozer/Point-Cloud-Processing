import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# קריאת נתוני הקובץ
file_path = "input.csv"
data = pd.read_csv(file_path)

# הנחת עבודה שהעמודה עם הערכים היא 'z'
z_values = data['z']

# חישוב מדדים מרכזיים עבור ערכי ה-z
mean_z = np.mean(z_values)
median_z = np.median(z_values)
std_z = np.std(z_values)
min_z = np.min(z_values)
max_z = np.max(z_values)

# הדפסת המדדים המרכזיים
print(f"Mean Z: {mean_z}")
print(f"Median Z: {median_z}")
print(f"Standard Deviation of Z: {std_z}")
print(f"Min Z: {min_z}")
print(f"Max Z: {max_z}")

# חיפוש הערכים הגדולים ביותר שנמצאים מעל לערך X, לדוגמה 1
highest_value_above_0 = z_values[z_values >0].min()
print(f"The highest value below 1 is: {highest_value_above_0}")

# ניתוח האם יש ערכים בין 0.1 ל-0.2
values_between_01_and_02 = z_values[(z_values > 0.1) & (z_values < 1)]
print(f"Values between 0.1 and 1: {values_between_01_and_02}")

# הצגת גרף התפלגות עבור ערכי ה-z
plt.hist(z_values, bins=50, color='blue', alpha=0.7)
plt.title('Distribution of Z values')
plt.xlabel('Z values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
