import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# קריאת הנתונים
file_path = "input.csv"
data = pd.read_csv(file_path)

# נניח שאתה משתמש בעמודה 'Probability of False Alarm' מהנתונים
pfa_values = data['Probability of False Alarm'].values

# מצא את כל הערכים שמפחות מ-1
values_below_1 = pfa_values[pfa_values < 1]

# מצא את הערך הגבוה ביותר אחרי 1
highest_value_below_1 = np.max(values_below_1)

print(f"The highest value below 1 is: {highest_value_below_1}")
