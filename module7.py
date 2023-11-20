import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score


class KNNRegression:
    def __init__(self, k):
        # Initialize the KNNRegression object with an empty array for points and the specified value of k.
        self.points = np.array([])
        self.k = k
        self.knn_model = KNeighborsRegressor(n_neighbors=k)

    def add_point(self, x, y):
        # Add a new point (x, y) to the dataset.
        point = np.array([x, y])
        if self.points.size:
            self.points = np.vstack([self.points, point])
        else:
            self.points = point.reshape(1, -1)

        # Update the KNeighborsRegressor model with the new data.
        self.knn_model.fit(self.points[:, 0].reshape(-1, 1), self.points[:, 1])

    def get_knn_regression(self, x):
        # Get the k-nearest neighbors regression for a given x value.
        if self.k > len(self.points):
            raise ValueError("number of points is less than k")

        # Predict the y value using the trained KNeighborsRegressor model.
        predicted_y = self.knn_model.predict(np.array(x).reshape(-1, 1))

        # Calculate and return the predicted y value and the coefficient of determination (R^2).
        r_squared = r2_score(self.points[:, 1], self.knn_model.predict(
            self.points[:, 0].reshape(-1, 1)))
        return predicted_y[0], r_squared


N = int(input("Enter the number of points: "))
k = int(input("Enter the value of k: "))

knn = KNNRegression(k)

for i in range(N):
    x = float(input(f"Enter x value of point {i + 1}: "))
    y = float(input(f"Enter y value of point {i + 1}: "))
    knn.add_point(x, y)

x = float(input("Enter the value of x for prediction: "))

result, r_squared = knn.get_knn_regression(x)
print("Predicted y: ", result)
print("R squared: ", r_squared)
