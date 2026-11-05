JUPYTERLAB VERSION
==================

Open `email_spam_knn_svm.ipynb` in JupyterLab. Run cells from top to bottom (Shift+Enter), or use Kernel > Restart Kernel and Run All Cells.

Keep `emails.csv` in this same folder. The notebook uses a relative filename to load it.

If a required package is missing, run `%pip install pandas numpy scikit-learn matplotlib scipy` in a notebook cell, then restart the kernel.

EXPERIMENT 8 - EMAIL SPAM DETECTION USING KNN AND SVM

Aim:
Classify email as Normal/Not Spam (0) or Spam (1), using KNN and SVM.

Dataset:
emails.csv (5,172 rows, 3,002 columns).

IMPORTANT DATASET DIFFERENCE:
This uploaded CSV is NOT a raw-message dataset. It already contains:
- Email No. : identifier (not used as a feature)
- 3,000 numeric word-frequency columns: input features
- Prediction : target (0 = Not Spam, 1 = Spam)

So do NOT use TfidfVectorizer or columns named "message" and "label" with
this particular file. The code trains directly on its numeric features.

Run:
python email_spam_knn_svm.py

The program reports confusion matrix, accuracy, error rate, precision,
recall and F1 score for both classifiers.
