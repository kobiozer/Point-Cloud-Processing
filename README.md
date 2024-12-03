# Point-Cloud-Processing

This project implements cone detection in 3D point cloud data using Python. The approach involves clustering the points with DBSCAN and applying geometric analysis to identify clusters resembling cones.

## Operating System
This project was developed and tested on Windows 10.

## Installation and Running Instructions

### Prerequisites
- Python 3.8 or above
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
