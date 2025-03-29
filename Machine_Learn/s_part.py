import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import pandas as pd
import random
import time
import f_part as gauss
class k_medoid():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gaussian Dataset Generator")

        # Matplotlib Figure and Canvas
        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        try:
            self.dataset = pd.read_csv("Machine_Learn/dataset.txt", sep="\s+", names=["x", "y", "regiunepip3"])
            print("List AVAILABLE")
        except:
            print("List N/A")

        self.k = "K = N\A"

        self.k_med_x = []
        self.k_med_y = []
        self.dist_tmp = []
        self.dataset_choice = []

        self.colors = ['blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'black', 'brown', 'red']

        self.fig.clf()
        self.ax = self.fig.add_subplot(111)

    def build(self):
        self.fig.clf()
        self.ax = self.fig.add_subplot(111)

        self.k_med_x.clear()
        self.k_med_y.clear()
        self.dataset_choice.clear()

        with open("Machine_Learn/dataset_choice.txt", "w") as f:
            print("Hello")

        self.dataset = pd.read_csv("Machine_Learn/dataset.txt", sep="\s+", names=["x", "y", "regiunepip3"])

        self.ax.scatter(self.dataset["x"], self.dataset["y"], c="blue", s=10, label="Puncte")

        self.ax.set_xlabel('X Coordinate')
        self.ax.set_ylabel('Y Coordinate')
        self.ax.set_title('Gaussian Distributed Points')
        self.ax.legend()
        self.ax.grid(True)
        
        for i in range(self.k):
            rnd_term = random.randrange(0, 10000, 1)
            dtx1 = self.dataset["x"][rnd_term]
            dty1 = self.dataset["y"][rnd_term]

            self.k_med_x.append(dtx1)
            self.k_med_y.append(dty1)

        self.ax.scatter(self.k_med_x, self.k_med_y, c="red", s=100, marker='x')
        print("medoid list x", self.k_med_x)

        for i in range(len(self.dataset)):
            for j in range(len(self.k_med_x)):
                dist = abs(self.k_med_x[j] - self.dataset["x"][i]) + abs(self.k_med_y[j] - self.dataset["y"][i])
                self.dist_tmp.append(dist)

            f_med = self.dist_tmp.index(min(self.dist_tmp))
            self.dataset_choice.append(f_med) # 10000
            self.dist_tmp.clear()
    
        with open("Machine_Learn/dataset_choice.txt", "w") as f:
            for k in self.dataset_choice:
                f.write(f"{k}\n")

        self.canvas.draw()

    def group(self):
        self.fig.clf()
        self.ax = self.fig.add_subplot(111)
        tmp_l_x = []
        tmp_l_y = []

        for i in range(len(self.k_med_x)):   # i = 0 --> 6   (for medoid = 7)
            tmp_l_x = []
            tmp_l_y = []
            for j in range(len(self.dataset_choice)):  # j --> 10 000
                if self.dataset_choice[j] == i:  # if index of 10 000 == k medoid(0--->6)
                    tmp_l_x.append(self.dataset["x"][j])
                    tmp_l_y.append(self.dataset["y"][j])
            self.ax.scatter(tmp_l_x, tmp_l_y, c=self.colors[i], s=10, label=f"Group {i}")

        for i in range(len(self.k_med_x)):
            self.ax.scatter(self.k_med_x[i], self.k_med_y[i], c="red", s=100, marker='x')

        self.canvas.draw()

    def plot_group(self):
        self.n_center_grav_x = []
        self.n_center_grav_y = []
        for i in range(len(self.k_med_x)):   # i = 0 --> 6   (for medoid = 7)
            tmp_l_x = []
            tmp_l_y = []
            for j in range(len(self.dataset_choice)):  # j --> 10 000
                if self.dataset_choice[j] == i:  # if index of 10 000 == k medoid(0--->6)
                    tmp_l_x.append(self.dataset["x"][j])
                    tmp_l_y.append(self.dataset["y"][j])
            self.n_center_grav_x.append(sum(tmp_l_x)/len(tmp_l_x))
            self.n_center_grav_y.append(sum(tmp_l_y)/len(tmp_l_y))
            self.ax.scatter(tmp_l_x, tmp_l_y, c=self.colors[i], s=10, label=f"Group {i}")
        self.canvas.draw()

    def k_gen(self):
        self.k = random.randrange(2, 10, 1)
        print(self.k)

        self.k_label.config(text=str(self.k))

    def epoch_try(self):
        print("Epoch")
        self.fig.clf()
        self.ax = self.fig.add_subplot(111)
        self.n_center_grav_x = []
        self.n_center_grav_y = []

        for i in range(len(self.k_med_x)):   # i = 0 --> 6   (for medoid = 7)
            tmp_l_x = []
            tmp_l_y = []
            for j in range(len(self.dataset_choice)):  # j --> 10 000
                if self.dataset_choice[j] == i:  # if index of 10 000 == k medoid(0--->6)
                    tmp_l_x.append(self.dataset["x"][j])
                    tmp_l_y.append(self.dataset["y"][j])
                    
            temp_grav_x = sum(tmp_l_x)/len(tmp_l_x)
            temp_grav_y = sum(tmp_l_y)/len(tmp_l_y)

            closest_value_x = min(tmp_l_x, key=lambda x: abs(x - temp_grav_x))
            #closest_value_y = min(tmp_l_y, key=lambda x: abs(x - temp_grav_y))
            print(f"The closest value to target value {temp_grav_x} is {closest_value_x}")
            print(f"Group {i}")
            print(f"closest value it is at index {tmp_l_x.index(closest_value_x)}")

            tmp_l_x.index(closest_value_x)
            self.n_center_grav_x.append(tmp_l_x[tmp_l_x.index(closest_value_x)])
            self.n_center_grav_y.append(tmp_l_y[tmp_l_x.index(closest_value_x)])
            self.ax.scatter(tmp_l_x, tmp_l_y, c=self.colors[i], s=10, label=f"Group {i}")

        print(self.n_center_grav_x, self.n_center_grav_y)    
        self.ax.scatter(self.n_center_grav_x, self.n_center_grav_y, c="red", s=200, marker='x')

        print("New center of grav found")

        self.dataset_choice.clear()

        for i in range(len(self.dataset)):  # i = 0 --> 10 000
            for j in range(len(self.n_center_grav_x)): # j = 0 --> kmedoid (ex.7 [max 10])
                dist = abs(self.n_center_grav_x[j] - self.dataset["x"][i]) + abs(self.n_center_grav_y[j] - self.dataset["y"][i])
                self.dist_tmp.append(dist)

            f_med = self.dist_tmp.index(min(self.dist_tmp))
            self.dataset_choice.append(f_med) # 10000

            self.dist_tmp.clear()
        print("New dist and choice calculated for each point")

        dist_tmp = []
        dist = 0
        distf = 0
        for i in range(len(self.n_center_grav_x)):   # i = 0 --> 6   (for medoid = 7)
            for j in range(len(self.dataset_choice)):  # j --> 10 000
                if self.dataset_choice[j] == i:  # if index of 10 000 == k medoid(0--->6)
                    #print(f"index j = {j}, list n_center_grav = {self.n_center_grav_x}")
                    dist = abs(self.n_center_grav_x[i] - self.dataset["x"][j]) + abs(self.n_center_grav_y[i] - self.dataset["y"][j])
                    distf = distf + dist
            dist_tmp.append(distf)
        e_cvg = sum(dist_tmp)
        print("Error cvg calculated")

        tmp_l_x = []
        tmp_l_y = []

        for i in range(len(self.n_center_grav_x)):   # i = 0 --> 6   (for medoid = 7)
            tmp_l_x = []
            tmp_l_y = []
            for j in range(len(self.dataset_choice)):  # j --> 10 000
                if self.dataset_choice[j] == i:  # if index of 10 000 == k medoid(0--->6)
                    tmp_l_x.append(self.dataset["x"][j])
                    tmp_l_y.append(self.dataset["y"][j])
            self.ax.scatter(tmp_l_x, tmp_l_y, c=self.colors[i], s=10, label=f"Group {i}")
        
        self.ax.scatter(self.n_center_grav_x, self.n_center_grav_y, c="red", s=300, marker='x', )

        self.canvas.draw()

        print("Finish")
        print(f"Error {e_cvg}")

    def run_sgui(self):
        generate_k = tk.Button(self.root, text="K Generator", command=self.k_gen)
        generate_k.grid(row=3, column=0, pady=10)

        self.k_label = tk.Label(self.root, text=str(self.k))
        self.k_label.grid(row=4, column=0)

        generate_btn = tk.Button(self.root, text="Show plot",  command=self.build)
        generate_btn.grid(row=3, column=1, pady=10)

        group_btn = tk.Button(self.root, text="Group", command=self.group)
        group_btn.grid(row=3, column=2, padx=10)

        an = tk.Button(self.root, text="Regenerate", command=gauss.run_gui)
        an.grid(row=1, column=0, padx=10)

        an2 = tk.Button(self.root, text="Epoch", command=self.epoch_try)
        an2.grid(row=1, column=1, padx=10)

        self.root.mainloop()

myobj = k_medoid()
myobj.run_sgui()