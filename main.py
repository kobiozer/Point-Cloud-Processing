import pandas as pd
import numpy as np
import open3d as o3d
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# קריאת הנתונים
file_path = "input.csv"
data = pd.read_csv(file_path)

# סינון הנתונים לפי 'Probability of False Alarm' ו-'z'
highest_value_below_1 = 0.09
filtered_data = data[(data['Probability of False Alarm'] <= highest_value_below_1) & (data['z'] > 0.5)]
print(f"Number of points after filtering: {len(filtered_data)}")


# יצירת מערך תלת-ממדי של נקודות
points = filtered_data[['x', 'y', 'z']].values
print(f"Number of points for clustering: {len(points)}")

# נרמול הנתונים
points_normalized = StandardScaler().fit_transform(points)

# ביצוע קלאסטרינג עם DBSCAN
db = DBSCAN(eps=0.2, min_samples=75)
db.fit(points_normalized)
labels = db.labels_

# חישוב מספר הקלאסטרים ונקודות הרעש
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"Number of clusters: {n_clusters}")
print(f"Number of noise points: {n_noise}")

# יצירת צבעים לכל קלאסטר
colors = np.random.rand(len(set(labels)) - (1 if -1 in labels else 0), 3)

# הצבת צבע לכל נקודה לפי הקלאסטר שלה (אם היא רעש, צבע לבן)
colored_points = np.array([colors[label] if label != -1 else [1, 1, 1] for label in labels])

# יצירת ענן נקודות
point_cloud = o3d.geometry.PointCloud()

# הצגת צבעים ונקודות
point_cloud.points = o3d.utility.Vector3dVector(points)
point_cloud.colors = o3d.utility.Vector3dVector(colored_points)


# הצגת ענן הנקודות בתלת-מימד
o3d.visualization.draw_geometries([point_cloud], window_name="Point Cloud with Clusters")


