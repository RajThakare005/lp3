LP3 ML PRACTICALS - JUPYTERLAB PACK
====================================

This pack contains the five ML experiments from the LP3 chit.

FOLDERS
-------
01_Uber_Fare_Prediction
02_Email_Spam_Classification
03_Bank_Customer_Churn_ANN
04_Diabetes_KNN_Classification
05_Sales_Clustering_KMeans_and_Hierarchical

Each folder contains:
- A Jupyter Notebook (.ipynb) split into cells.
- The matching CSV dataset.
- A .txt copy of the code.
- README.txt with experiment instructions.

HOW TO RUN IN JUPYTERLAB
------------------------
1. Extract this ZIP.
2. Open JupyterLab.
3. Navigate to the desired experiment folder.
4. Open its .ipynb notebook.
5. Run cells from top to bottom (Shift+Enter), or select Kernel > Restart Kernel and Run All Cells.

If a package is missing, run this in a notebook cell:
    %pip install pandas numpy scikit-learn matplotlib scipy
Then restart the kernel and run all cells.

DATASET-SPECIFIC NOTES
----------------------
- Email CSV already contains numeric word-frequency columns. Prediction is the
  target (0=Not Spam, 1=Spam); TfidfVectorizer is not applicable to this CSV.
- Bank ANN uses scikit-learn MLPClassifier, an Artificial Neural Network model.
- Diabetes program imputes zero-coded missing values in selected measurement columns.
- Sales K-Means uses the Elbow Method for K=1..10; FINAL_K=3 is an example.
  The optional Hierarchical notebook includes a dendrogram.
- Uber data is cleaned for missing/invalid fare, passenger and GPS records.

Dependencies:
pandas, numpy, scikit-learn, matplotlib, scipy
