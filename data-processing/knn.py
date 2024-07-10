# VERSION Python 3.11.4

from sklearn.neighbors import NearestNeighbors
import numpy as np

def knn(RSSI_train, RSSI_test, k): # location indices are implicit
    """
    Perform k-nearest neighbors classification.

    Parameters:
    RSSI_train (array-like): Training data features.
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

    # LOCATION IS IMPLICIT
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
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(RSSI_train)
    distances, indices = nbrs.kneighbors(RSSI_test)
    print("DIST:")
    print(distances)
    print()
    print("INDEX: ")
    print(indices)
if __name__ == "__main__":
    RSSI_train = np.array([[-60, -65, -70], [-55, -60, -75], [-50, -55, -80]])
    RSSI_test = np.array([[-58, -63, -68], [-53, -58, -73]])
    knn(RSSI_train, RSSI_test, 2)