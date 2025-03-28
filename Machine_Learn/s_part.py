import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import pandas as pd
import random
import time

global k_med_x, k_med_y, k

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


    global k_med_x, k_med_y, k
    k_med_x = []
    k_med_y = []
    dist_tmp = []
    dataset_choice = []
    
    k = random.randrange(2, 10, 1)
    # k = 3
    print("K = ", k)
    for i in range(k):
        rnd_term = random.randrange(0, 10000, 1)
        dtx1 = dataset["x"][rnd_term]
        dty1 = dataset["y"][rnd_term]

        k_med_x.append(dtx1)
        k_med_y.append(dty1)

        #print("dt1", dt1, type(dt1))
        #print("dataset ", dataset["x"])
        ax.scatter(dtx1, dty1, c="red", s=100, marker='x')
    
    print("medoid list x", k_med_x)

    for i in range(len(dataset)):
        for j in range(len(k_med_x)):
            dist = abs(k_med_x[j] - dataset["x"][i]) + abs(k_med_y[j] - dataset["y"][i])
            #print("kmedx", k_med_x[j], "dataset x", dataset["x"][i], "Manhattan Distance", dist)
            dist_tmp.append(dist)
            #print("Manhattan Distance Medoid List", dist_tmp)

        #print("min", min(dist_tmp))
        f_med = dist_tmp.index(min(dist_tmp))
        #print("Choss value", f_med)
        dataset_choice.append(f_med) # 10000
        #print("dataset choice", dataset_choice)
        dist_tmp.clear()

    with open("dataset_choice.txt", "w") as f:
        for k in dataset_choice:
            f.write(f"{k}\n")

    canvas.draw()

def group(fig, canvas):
    global k_med_x, k_med_y, k

    print("medoid list x", k_med_x)

    dataset = pd.read_csv("dataset.txt", sep="\s+", names=["x", "y", "regiunepip3"])

    dataset_choice = pd.read_csv("dataset_choice.txt", sep="\s+", names=["choice"])

    colors = ['blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'black', 'brown', 'red']

    # Clear the previous plot
    fig.clf()
    ax = fig.add_subplot(111)

    for i in range(len(dataset)): # 10 000
        ax.scatter(dataset["x"][i], dataset["y"][i], c=colors[dataset_choice["choice"][i]], s=10, label="Puncte")

    for i in range(len(k_med_x)):
        ax.scatter(k_med_x[i], k_med_y[i], c="red", s=100, marker='x')

    canvas.draw()


def run_sgui():
    def on_generate():
        build(fig, canvas)

    def on_group():
        group(fig, canvas)

    root = tk.Tk()
    root.title("Gaussian Dataset Generator")

    # Matplotlib Figure and Canvas
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Generate button
    generate_btn = tk.Button(root, text="Generate", command=on_generate)
    generate_btn.grid(row=3, column=0, columnspan=2, pady=10)

    group_btn = tk.Button(root, text="Group", command=on_group)
    group_btn.grid(row=3, column=1, columnspan=2, padx=10)

    root.mainloop()

run_sgui()