JUPYTERLAB VERSION
==================

Open `diabetes_knn.ipynb` in JupyterLab. Run cells from top to bottom (Shift+Enter), or use Kernel > Restart Kernel and Run All Cells.

Keep `diabetes.csv` in this same folder. The notebook uses a relative filename to load it.

If a required package is missing, run `%pip install pandas numpy scikit-learn matplotlib scipy` in a notebook cell, then restart the kernel.

EXPERIMENT 10 - DIABETES PREDICTION USING KNN

Aim:
Implement KNN on the diabetes dataset and calculate confusion matrix,
accuracy, error rate and precision.

Dataset:
diabetes.csv (768 rows, 9 columns).

Target:
Outcome (0 = Not Diabetic, 1 = Diabetic).

Dataset-specific note:
Zero in Glucose, BloodPressure, SkinThickness, Insulin and BMI is treated
as a missing measurement and replaced using the median. Zero Pregnancies
is retained because it can be valid.

Model:
KNeighborsClassifier with k=5. The pipeline performs median imputation,
StandardScaler and KNN.

Run:
python diabetes_knn.py
