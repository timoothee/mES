import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
import random

SIGMA = 5

def gauss(x, m, sigma):
    return np.exp(-((x - m) ** 2) / (2 * sigma ** 2))

def rand_x(mx, thrs_x):
    prob = 1
    thrs_x = 2
    while prob < thrs_x:
        x = np.random.uniform(-300, 300)  # Step 2
        prob = gauss(x, mx, SIGMA)       # Step 3 
        thrs_x = int(np.random.uniform(0, 1) * 1000) # Step 4
        thrs_x = thrs_x/1000
        print("x", x)
    else:
        return x
    
def rand_y(my, thrs_y):
    prob = 1
    thrs_y = 2
    while prob < thrs_y:
        y = np.random.uniform(-300, 300)
        thrs_y = int(np.random.uniform(0, 1) * 1000)
        thrs_y = thrs_y/1000
        prob = gauss(y, my, SIGMA)
    else:
        return y

def generate_gaussian_dataset(total_points, num_groups, canvas, fig):
    points = []
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'black', 'brown']

    for i in range(num_groups):
        print("Hello", i)
        mx = np.random.uniform(-300, 300)
        my = np.random.uniform(-300, 300)
        for _ in range(total_points):
            thrs_x = int(np.random.uniform(0, 1) * 1000)
            thrs_y = int(np.random.uniform(0, 1) * 1000)

            thrs_x = thrs_x/1000
            thrs_y = thrs_y/1000

            #print(thrs_x)
            set_x = rand_x(mx, thrs_x)
            set_y = rand_y(my, thrs_y)

            # Keep points within Cartesian bounds (-300, 300)
            # x = np.clip(set_x, -300, 300)
            # y = np.clip(set_y, -300, 300)

            x = set_x
            y = set_y

            points.append((x, y, i))

    # Save points to file
    with open("Machine_Learn/dataset.txt", "w") as f:
        for x, y, group in points:
            f.write(f"{x:.2f} {y:.2f} {group}\n")
    print("Values written")
    # Clear the previous plot
    fig.clf()
    ax = fig.add_subplot(111)

    # Plot the points
    for i, color in enumerate(colors[:num_groups]):
        group_points = [(x, y) for x, y, group in points if group == i]
        xs, ys = zip(*group_points)
        ax.scatter(xs, ys, color=color, s=5, label=f'Group {i}')

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Gaussian Distributed Points')
    ax.legend()
    ax.grid(True)

    # Refresh canvas
    canvas.draw()

def run_gui():
    def on_generate():
        try:
            total_points = int(points_entry.get())
            num_groups = int(groups_entry.get())
            if total_points <= 0 or num_groups <= 0:
                raise ValueError("Values must be positive integers.")
            generate_gaussian_dataset(total_points, num_groups, canvas, fig)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    root = tk.Tk()
    root.title("Gaussian Dataset Generator")

    # Matplotlib Figure and Canvas
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Input fields
    tk.Label(root, text="Total Points:").grid(row=1, column=0, padx=10, pady=5)
    points_entry = tk.Entry(root)
    points_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Number of Groups:").grid(row=2, column=0, padx=10, pady=5)
    groups_entry = tk.Entry(root)
    groups_entry.grid(row=2, column=1, padx=10, pady=5)

    # Generate button
    generate_btn = tk.Button(root, text="Generate", command=on_generate)
    generate_btn.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()