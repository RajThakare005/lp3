JUPYTERLAB VERSION
==================

Open `bank_churn_ann.ipynb` in JupyterLab. Run cells from top to bottom (Shift+Enter), or use Kernel > Restart Kernel and Run All Cells.

Keep `Churn_Modelling.csv` in this same folder. The notebook uses a relative filename to load it.

If a required package is missing, run `%pip install pandas numpy scikit-learn matplotlib scipy` in a notebook cell, then restart the kernel.

EXPERIMENT 9 - BANK CUSTOMER CHURN USING A NEURAL NETWORK

Aim:
Predict whether a bank customer will leave (Exited=1) or stay (Exited=0).

Dataset:
Churn_Modelling.csv (10,000 rows, 14 columns).

Preparation:
- Removes RowNumber, CustomerId and Surname.
- One-hot encodes Geography and Gender.
- Uses Exited as the target.
- Uses stratified train/test split and scales using training data only.

Network:
MLPClassifier with hidden layers (16, 8), ReLU activation and Adam optimizer.
This is an Artificial Neural Network implementation; TensorFlow is not
required for this version.

Run:
python bank_churn_ann.py

The PDF version used TensorFlow/Keras. This scikit-learn MLP version was
chosen to keep setup simpler while meeting the neural-network classifier aim.
