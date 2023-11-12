import numpy as np


class KNNRegression:

    def __init__(self, k):
        self.points = np.array([])
        self.k = k

    def add_point(self, x, y):
        point = np.array([x, y])
        if self.points.size:
            self.points = np.vstack([self.points, point])
        else:
            self.points = point

    def get_knn_regression(self, x):
        if self.k > len(self.points):
            raise ValueError("number of points is less than k")

        x_distances = np.abs(self.points[:, 0] - x)
        nearest_k_indices = np.argsort(x_distances)[:k]
        k_nearest_points = self.points[nearest_k_indices]
        y_values = k_nearest_points[:, 1]
        predicted_y = np.mean(y_values)
        return predicted_y


N = int(input("Enter the number of points: "))
k = int(input("Enter the value of k: "))

knn = KNNRegression(k)

for i in range(N):
    x = float(input(f"Enter x value of point {i + 1}: "))
    y = float(input(f"Enter y value of point {i + 1}: "))
    knn.add_point(x, y)

x = float(input("Enter the value of x for prediction: "))

result = knn.get_knn_regression(x)
print("Predicted y:", result)
