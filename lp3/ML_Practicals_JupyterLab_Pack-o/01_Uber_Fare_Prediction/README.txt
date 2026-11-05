JUPYTERLAB VERSION
==================

Open `uber_fare_prediction.ipynb` in JupyterLab. Run cells from top to bottom (Shift+Enter), or use Kernel > Restart Kernel and Run All Cells.

Keep `uber.csv` in this same folder. The notebook uses a relative filename to load it.

If a required package is missing, run `%pip install pandas numpy scikit-learn matplotlib scipy` in a notebook cell, then restart the kernel.

EXPERIMENT 7 - UBER FARE PREDICTION

Aim:
Predict Uber fare using Linear Regression and Random Forest Regression.

Dataset:
uber.csv (uploaded Uber dataset; 200,000 rows).

Features:
pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude,
passenger_count.
Target: fare_amount.

Dataset cleaning:
- Removes missing rows.
- Removes zero/negative fares and fares above 250.
- Keeps passenger counts from 1 to 6.
- Removes corrupted/out-of-area GPS coordinates using a New York area range.

Run:
python uber_fare_prediction.py

Output:
MSE and R2 score for both models, followed by a sample fare prediction.
