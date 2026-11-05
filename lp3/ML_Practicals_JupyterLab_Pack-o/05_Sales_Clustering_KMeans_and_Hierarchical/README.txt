JUPYTERLAB VERSION
==================

Open `sales_kmeans_elbow.ipynb` in JupyterLab. Run cells from top to bottom (Shift+Enter), or use Kernel > Restart Kernel and Run All Cells.

Keep `sales_data_sample.csv` in this same folder. The notebook uses a relative filename to load it.

If a required package is missing, run `%pip install pandas numpy scikit-learn matplotlib scipy` in a notebook cell, then restart the kernel.

EXPERIMENT 11 - SALES DATA CLUSTERING

Aim:
Implement clustering on sales_data_sample.csv and determine the cluster
count using the Elbow Method.

Dataset:
sales_data_sample.csv (2,823 rows, 25 columns; Latin-1 encoding).

Main program: sales_kmeans_elbow.py
- Uses QUANTITYORDERED, PRICEEACH, SALES and MSRP.
- Scales the four numerical features.
- Calculates WCSS for K=1 to K=10 and plots the Elbow graph.
- Runs K-Means with FINAL_K=3 as an example. Inspect the graph and change
  FINAL_K if your elbow suggests a different value.

Optional alternative: sales_hierarchical.py
- Performs Agglomerative (Hierarchical) Clustering using Ward linkage.
- Displays a dendrogram to help choose the cluster count.
- FINAL_K is set to 3 as an example.

Run K-Means:
python sales_kmeans_elbow.py

Run Hierarchical:
python sales_hierarchical.py
