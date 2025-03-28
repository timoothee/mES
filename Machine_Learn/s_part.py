import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import pandas as pd
import random


def build(fig, canvas):
    points_list = []
    num_groups = 5

    dataset = pd.read_csv("dataset.txt", sep="\s+", names=["x", "y", "regiunepip3"])

    colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'black', 'brown']

    # Clear the previous plot
    fig.clf()
    ax = fig.add_subplot(111)

    # Plot the points
    #for i, color in enumerate(colors[:num_groups]):
    #    group_points = [(x, y) for x, y, group in points_list if group == i]
    #    xs, ys = zip(*group_points)
    #    ax.scatter(xs, ys, color=color, s=5, label=f'Group {i}')

    ax.scatter(dataset["x"], dataset["y"], c="blue", s=10, label="Puncte")

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Gaussian Distributed Points')
    ax.legend()
    ax.grid(True)

    
    
    k = random.randrange(2, 10, 1)
    print("K = ", k)
    for i in range(k):
        rnd_term = random.randrange(0, 10000, 1)
        dtx1 = dataset["x"][rnd_term]
        dty1 = dataset["y"][rnd_term]
        #print("dt1", dt1, type(dt1))
        #print("dataset ", dataset["x"])
        ax.scatter(dtx1, dty1, c="red", s=100, marker='x')
    
    canvas.draw()

def run_sgui():
    def on_generate():
        build(fig, canvas)

    root = tk.Tk()
    root.title("Gaussian Dataset Generator")

    # Matplotlib Figure and Canvas
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Generate button
    generate_btn = tk.Button(root, text="Generate", command=on_generate)
    generate_btn.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

run_sgui()