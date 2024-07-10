# VERSION Python 3.11.4

from sklearn.neighbors import NearestNeighbors
import numpy as np

def knn(RSSI_train, LOCATION_train, RSSI_test, k):
    """
    Perform k-nearest neighbors classification.

    Parameters:
    RSSI_train (array-like): Training data features.
    LOCATION_train (array-like): Training data labels.
    RSSI_test (array-like): Test data features.
    k (int): Number of neighbors to consider.

    Returns:
    array-like: Predicted labels for the test data.
    
    Sample training data
    RSSI_train = [
        [-60, -65, -70],  # RSSI values from 3 beacons for sample 1
        [-55, -60, -75],  # RSSI values from 3 beacons for sample 2
        # ...
    ]

    LOCATION_train = [
        1,  # Location label for sample 1
        2,  # Location label for sample 2
        # ...
    ]

    # Sample test data
    RSSI_test = [
        [-58, -63, -68],  # RSSI values from 3 beacons for test sample 1
        [-53, -58, -73],  # RSSI values from 3 beacons for test sample 2
        # ...
    ]

    label_test = [
        1,  # Location label for test sample 1
        2,  # Location label for test sample 2
        # ...
    ]
    """
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)