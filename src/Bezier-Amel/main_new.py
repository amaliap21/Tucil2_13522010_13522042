import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def bezier_divide_and_conquer(points, t):
    if len(points) == 1:
        return points[0]
    else:
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - t) * points[i][0] + t * points[i + 1][0]
            y = (1 - t) * points[i][1] + t * points[i + 1][1]
            new_points.append((x, y))
        return bezier_divide_and_conquer(new_points, t)

def draw_bezier():
    global control_points
    # Clear previous curve
    plt.clf()
    bezier_points = [bezier_divide_and_conquer(control_points, t) for t in np.linspace(0, 1, 100)]
    x_vals, y_vals = zip(*bezier_points)
    # Plot Bezier curve
    plt.plot(x_vals, y_vals, label="Bezier Curve")
    # Plot control points
    plt.plot(*zip(*control_points), 'ro-', label="Control Points")
    plt.legend()
    canvas.draw()

def add_points():
    global control_points
    control_points = []
    num_of_points = simpledialog.askinteger("Input", "How many points?", parent=root)
    if num_of_points:
        for _ in range(num_of_points): # PERBAIKI jadi for _ aja
            x, y = simpledialog.askstring("Input", "Enter point (x,y):", parent=root).split(',')
            control_points.append((int(x), int(y)))
            draw_bezier()  # Automatically draw the curve after points are added
            # print(f"iteration {i+1} of {num_of_points}")

root = tk.Tk()
root.title("Bezier Curve Drawer")

# Setup Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
widget = canvas.get_tk_widget()
widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

control_points = []

btn_add_points = tk.Button(root, text="Add Points", command=add_points)
btn_add_points.pack(side=tk.LEFT, pady=20, padx=10)

# btn_draw_curve = tk.Button(root, text="Draw Bezier Curve", command=draw_bezier)
# btn_draw_curve.pack(side=tk.LEFT, pady=20, padx=10)

root.mainloop()
