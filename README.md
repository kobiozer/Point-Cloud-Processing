# Point-Cloud-Processing

This project implements cone detection in 3D point cloud data using Python. The approach involves clustering the points with DBSCAN and applying geometric analysis to identify clusters resembling cones.

## Operating System
This project was developed and tested on Windows 10.

## Installation and Running Instructions

### Prerequisites 
- Python 3.9
- Required Python packages:
  - numpy == 1.23.5
  - pandas
  - open3d
  - scikit-learn

Install dependencies using pip:
```bash
pip install -r requirements.txt

After installing the dependencies, you can run the main script:
python main.py

This will execute the cone detection algorithm on the input point cloud data- input.csv


Project Explanation:
During the project, I focused on data processing, filtering, and visualization. Initially, I created test files to analyze the data and identify appropriate values for filtering. The main goal was to process data from a CSV file and remove irrelevant points based on specific criteria.
After filtering the data, I used the DBSCAN clustering algorithm to identify groups of similar data points. Open3D was employed for 3D visualization to explore the shape and arrangement of the data.
Overall, the project focused on detecting significant data clusters within a 3D point cloud and visualizing the results of the data analysis.

