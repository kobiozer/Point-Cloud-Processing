import pandas as pd
import numpy as np
import open3d as o3d
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Reading the data
file_path = "input.csv"
data = pd.read_csv(file_path)

# Filtering the data by 'Probability of False Alarm' and 'z'
highest_value_below_1 = 0.09
filtered_data = data[(data['Probability of False Alarm'] <= highest_value_below_1) & (data['z'] > 0.5)]
print(f"Number of points after filtering: {len(filtered_data)}")


# Creating a 3D array of points
points = filtered_data[['x', 'y', 'z']].values
print(f"Number of points for clustering: {len(points)}")

# Normalizing the data
points_normalized = StandardScaler().fit_transform(points)

# Performing clustering with DBSCAN
db = DBSCAN(eps=0.2, min_samples=75)
db.fit(points_normalized)
labels = db.labels_

# Calculating the number of clusters and noise points
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"Number of clusters: {n_clusters}")
print(f"Number of noise points: {n_noise}")

# Generating colors for each cluster
colors = np.random.rand(len(set(labels)) - (1 if -1 in labels else 0), 3)

# Assigning color to each point based on its cluster (white for noise points)
colored_points = np.array([colors[label] if label != -1 else [1, 1, 1] for label in labels])

# Creating a point cloud
point_cloud = o3d.geometry.PointCloud()

# Setting the points and colors
point_cloud.points = o3d.utility.Vector3dVector(points)
point_cloud.colors = o3d.utility.Vector3dVector(colored_points)


# Displaying the point cloud in 3D
o3d.visualization.draw_geometries([point_cloud], window_name="Point Cloud with Clusters")


