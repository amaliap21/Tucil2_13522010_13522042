import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import time
from BruteForce import bezier_brute_force
from DivideAndConquer import bezier_divide_and_conquer

# Opsi Algoritma
def choose_algorithm():
    response = simpledialog.askstring("Choose Algorithm", "Enter 'BF' for Brute Force or 'DAC' for Divide and Conquer:", parent=root)
    return response.strip().upper()

# Gambar Kurva Bezier
def draw_bezier():
    global control_points
    plt.clf()
    plt.plot(*zip(*control_points), marker='o', color='peachpuff', linestyle='-', label="Control Points")

    # Pilih Algoritma
    alg_choice = choose_algorithm()

    # Waktu Mulai
    start = time.time()

    # Plot Sesuai Algoritma yang Dipilih
    if alg_choice == 'BF':
        t_values = np.linspace(0, 1, 100)
        bezier_points = [bezier_brute_force(control_points, t) for t in t_values]
        plt.plot(*zip(*bezier_points), marker='o', linestyle='-', label="Bezier Curve\n(Brute Force)")
    elif alg_choice == 'DAC':
        # Plot Bezier curve
        BezierPoints, MiddlePoints = bezier_divide_and_conquer(control_points, 0, 5)
        plt.plot(*zip(*MiddlePoints), marker = 'o', color = 'palegreen', linestyle = 'dotted', label="Pass 1 Middle Points")
        plt.plot(*zip(*BezierPoints), marker = 'o', color = 'lightblue', linestyle = 'dashed', label="Pass 1 Bezier Curve\n(Divide and Conquer)")
        BezierPoints, MiddlePoints = bezier_divide_and_conquer(BezierPoints, 0, 5)
        plt.plot(*zip(*MiddlePoints), marker = 'o', color = 'pink', linestyle = 'dashed', label="Pass 2 Middle Points")
        plt.plot(*zip(*BezierPoints), marker = 'o', color='crimson', linestyle = 'solid', label="Pass 2 Bezier Curve\n(Divide and Conquer)")
    else:
        print("Invalid algorithm choice. Please enter 'BF' for Brute Force or 'DAC' for Divide and Conquer.")
        return

    # Waktu Eksekusi dan Tampilkan Hasil
    execution_time = time.time() - start
    algorithm_name = "Brute Force" if alg_choice == 'BF' else "Divide and Conquer"
    plt.title(f"Bezier Curve ({algorithm_name}) - Execution Time: {execution_time:.2f} seconds")
    plt.legend()
    canvas.draw()

# Gambar Titik
def add_points():
    global control_points
    control_points = []
    num_of_points = simpledialog.askinteger("Input", "How many points?", parent=root)
    if num_of_points:
        for _ in range(num_of_points):
            x, y = simpledialog.askstring("Input", "Enter point (x,y):", parent=root).split(',')
            control_points.append((float(x), float(y)))
    draw_bezier()

# Judul dan Tampilan GUI
root = tk.Tk()
root.title("Bezier Curve Drawer")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
widget = canvas.get_tk_widget()
widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

control_points = []

btn_add_points = tk.Button(root, text="Add Points", command=add_points)
btn_add_points.pack(side=tk.LEFT, pady=20, padx=10)

root.mainloop()