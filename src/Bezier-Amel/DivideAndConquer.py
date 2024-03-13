import matplotlib.pyplot as plt
import numpy as np

def bezier_divide_and_conquer(points, t):
    """
    Recursive function to calculate a point on a Bezier curve using
    the divide and conquer approach.

    :param points: Control points of the Bezier curve as a list of tuples/lists [(x1, y1), (x2, y2), ...].
    :param t: The parameter t, which varies between 0 and 1.
    :return: A point on the Bezier curve at the parameter t.
    """
    if len(points) == 1:
        return points[0]
    else:
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - t) * points[i][0] + t * points[i + 1][0]
            y = (1 - t) * points[i][1] + t * points[i + 1][1]
            new_points.append((x, y))
        return bezier_divide_and_conquer(new_points, t)

# Example control points
# (0, 0), (1, 2), (3, 3), (4, 0)
control_points = []
num_of_points = int(input("Masukkan jumlah titik: ")) 
for i in range(num_of_points):
    x, y = input("Masukkan titik (x, y): ").split()
    control_points.append((int(x), int(y)))

# Calculate points on the Bezier curve
bezier_points = [bezier_divide_and_conquer(control_points, t) for t in np.linspace(0, 1, 100)]

# Plotting
plt.figure()
x_vals, y_vals = zip(*bezier_points)
plt.plot(x_vals, y_vals, label="Bezier Curve")
plt.plot(*zip(*control_points), 'ro-', label="Control Points")
plt.legend()
plt.show()