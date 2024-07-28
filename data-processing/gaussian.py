from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
<<<<<<< HEAD
import numpy as np

def gaussian(x, y):
    """
    Fit a Gaussian Process Regressor to the provided data and make predictions.

    This function creates a Gaussian Process Regressor using an RBF kernel, fits it to the input data `x` and target values `y`, 
    and then makes predictions on the test data `X_test`.

    Parameters:
    x (array-like): The input data to fit the Gaussian Process Regressor. (i.e location ID or x,y coords)
    y (array-like): The target values corresponding to the input data. (i.e RSSI values)

    Returns:
    y_pred (array-like): The predicted values for the test input data `X_test`.
    """
    # Create a Gaussian process regressor with an RBF kernel
    kernel = RBF() # Research states the kind of kernel doesn't really matter
    gp = GaussianProcessRegressor(kernel=kernel)

    # Fit the Gaussian process regressor to your data
    gp.fit(x, y)

    # Predict using the trained Gaussian process regressor
    X_test = ...  # Your test input data
    y_pred = gp.sample_y(X_test, 1, random_state=42)

    # Print the predicted values
    return y_pred


if __name__ == "__main__":
    LOC_train = np.array([1, 2, 3])
    RSSI_train = np.array([[-60, -65, -70], [-55, -60, -75], [-50, -55, -80]])
    RSSI_test = np.array([[-58, -63, -68], [-53, -58, -73]])
    x = LOC_train  # Your input data
    y = RSSI_train  # Your target values
    print(gaussian(x, y))
=======

# Create a Gaussian process regressor with an RBF kernel
kernel = RBF()
gp = GaussianProcessRegressor(kernel=kernel)

# Define your input data and target values
X = ...  # Your input data
y = ...  # Your target values

# Fit the Gaussian process regressor to your data
gp.fit(X, y)

# Predict using the trained Gaussian process regressor
X_test = ...  # Your test input data
y_pred = gp.predict(X_test)

# Print the predicted values
print(y_pred)
>>>>>>> 5aafb513 (created gaussian.py file and add venv to gitignore)
