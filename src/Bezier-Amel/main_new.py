import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from DivideAndConquer import BezierSubdivision


def bezier_divide_and_conquer(points, reps, max_reps):
    if reps == max_reps:
        return points
    else:
        new_points = []
        new_points.append(points[0])
        for i in range(len(points) - 1):
            x = 0.5 * points[i][0] + 0.5 * points[i + 1][0]
            y = 0.5 * points[i][1] + 0.5 * points[i + 1][1]
            new_points.append((x, y))
        new_points.append(points[-1])
        reps += 1
        return bezier_divide_and_conquer(new_points, reps, max_reps)

def draw_bezier():
    global control_points
    # Clear previous curve
    plt.clf()
    # Plot control points
    plt.plot(*zip(*control_points), marker = 'o', color = 'peachpuff', linestyle = 'solid', label="Control Points")
    # Plot Bezier curve
    BezierPoints, MiddlePoints = BezierSubdivision(control_points, 0, 5)
    plt.plot(*zip(*MiddlePoints), marker = 'o', color = 'palegreen', linestyle = 'dotted', label="Pass 1 Middle Points")
    plt.plot(*zip(*BezierPoints), marker = 'o', color = 'lightblue', linestyle = 'dashed', label="Pass 1 Bezier Curve")
    BezierPoints, MiddlePoints = BezierSubdivision(BezierPoints, 0, 5)
    plt.plot(*zip(*MiddlePoints), marker = 'o', color = 'pink', linestyle = 'dashed', label="Pass 2 Middle Points")
    plt.plot(*zip(*BezierPoints), marker = 'o', color='crimson', linestyle = 'solid', label="Pass 2 Bezier Curve")
    plt.legend()
    canvas.draw()

def add_points():
    global control_points
    control_points = []
    num_of_points = simpledialog.askinteger("Input", "How many points?", parent=root)
    if num_of_points:
        for _ in range(num_of_points): # PERBAIKI jadi for _ aja
            x, y = simpledialog.askstring("Input", "Enter point (x,y):", parent=root).split(',')
            control_points.append((float(x), float(y)))
    draw_bezier()
            # print(f"iteration {i+1} of {num_of_points}")

root = tk.Tk()
root.title("Bezier Curve Drawer")

# Setup Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
widget = canvas.get_tk_widget()
widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

control_points = []
Controls = []

btn_add_points = tk.Button(root, text="Add Points", command=add_points)
btn_add_points.pack(side=tk.LEFT, pady=20, padx=10)

# btn_draw_curve = tk.Button(root, text="Draw Bezier Curve", command=draw_bezier)
# btn_draw_curve.pack(side=tk.LEFT, pady=20, padx=10)

root.mainloop()
