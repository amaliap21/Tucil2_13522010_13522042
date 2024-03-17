import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import time
import os
from BruteForce import bezier_brute_force
from DivideAndConquer import bezier_divide_and_conquer
from utils import update_folder_numbers, move_pycache_to_bin

# Inisialisasi jumlah folder output
base_output_path = './test/Output'
num_of_folders = update_folder_numbers(base_output_path)

##### ALGORITMA UTAMA #####
# Opsi Algoritma
def choose_algorithm():
    response = simpledialog.askstring("Choose Algorithm", "Enter 'BF' for Brute Force or 'DAC' for Divide and Conquer:", parent=root)
    return response.strip().upper()

# Gambar Kurva Bezier
def draw_bezier():
    global control_points
    global alg_choice
    global execution_time

    plt.clf()
    plt.plot(*zip(*control_points), marker='o', color='peachpuff', linestyle='-', label="Control Points")

    # Waktu Mulai
    start = time.time()

    # Plot Sesuai Algoritma yang Dipilih
    if alg_choice == 'BF':
        t_values = np.linspace(0, 1, 100)
        bezier_points = [bezier_brute_force(control_points, t) for t in t_values]
        execution_time += (time.time() - start) * 1000

        plt.plot(*zip(*bezier_points), marker='o', linestyle='-', label="Bezier Curve\n(Brute Force)")

    elif alg_choice == 'DAC':
        if len(control_points) < 3:
            pass
        else:
            BezierPoints, MiddlePoints, MiddlePointsLeft, MiddlePointsRight = bezier_divide_and_conquer(control_points, 1)
            execution_time += (time.time() - start) * 1000
            
            for i in range (len(MiddlePoints)):
                if (i == len(MiddlePoints) - 1):
                    plt.plot(*zip(*MiddlePoints[i]), marker = 'o', color = 'palegreen', linestyle = 'dashed', label="Mid Points")
                else:
                    plt.plot(*zip(*MiddlePoints[i]), marker = 'o', color = 'palegreen', linestyle = 'dashed')
            for i in range (len(MiddlePointsLeft)):
                if (i == len(MiddlePointsLeft) - 1):
                    plt.plot(*zip(*MiddlePointsLeft[i]), marker = 'o', color = 'lightblue', linestyle = 'dashed', label="Mid Points Left Curve")
                else:
                    plt.plot(*zip(*MiddlePointsLeft[i]), marker = 'o', color = 'lightblue', linestyle = 'dashed')
            for i in range (len(MiddlePointsRight)):
                if (i == len(MiddlePointsRight) - 1):
                    plt.plot(*zip(*MiddlePointsRight[i]), marker = 'o', color = 'pink', linestyle = 'dashed', label="Mid Points Right Curve")
                else:
                    plt.plot(*zip(*MiddlePointsRight[i]), marker = 'o', color = 'pink', linestyle = 'dashed')
            plt.plot(*zip(*BezierPoints), marker = 'o', color='crimson', label="Bezier Curve\n(Divide and Conquer)")      

    # Waktu Eksekusi dan Tampilkan Hasil
    algorithm_name = "Brute Force" if alg_choice == 'BF' else "Divide and Conquer"
    plt.title(f"Bezier Curve ({algorithm_name}) - Execution Time: {execution_time:.7f} milliseconds")
    plt.legend()
    canvas.draw()

# Gambar Titik
def add_points():
    global control_points
    global alg_choice
    global execution_time

    # Pilih Algoritma
    alg_choice = choose_algorithm()

    # Validasi Input Algoritma
    while (alg_choice != 'BF' and alg_choice != 'DAC'):
        alg_choice = choose_algorithm()

    control_points = []
    num_of_points = simpledialog.askinteger("Input", "How many points?", parent=root)
    if num_of_points:
        for i in range(num_of_points):
            x, y = simpledialog.askstring("Input", "Enter point (x,y):", parent=root).split(',')
            control_points.append((float(x), float(y)))
            draw_bezier()
            
            # Simpan Gambar
            name_algo = "Brute Force" if alg_choice == 'BF' else "Divide and Conquer"
            folder_name = f'./test/Output/{name_algo}/{num_of_folders[name_algo]}'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            if i != num_of_points - 1:
                plt.savefig(f'{folder_name}/BezierCurve ({i+1}).png')
            else:
                plt.savefig(f'{folder_name}/BezierCurve (final result).png')
                num_of_folders[name_algo] += 1
        # Reset waktu eksekusi
        execution_time = 0
        
# Judul dan Tampilan GUI
root = tk.Tk()
root.title("Bezier Curve Drawer")
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
widget = canvas.get_tk_widget()
widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

control_points = []
execution_time = 0

btn_add_points = tk.Button(root, text="Add Points", command=add_points)
btn_add_points.pack(side=tk.LEFT, pady=20, padx=10)

root.mainloop()

# Pindahkan __pycache__ ke bin
move_pycache_to_bin()