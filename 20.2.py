import tkinter as tk
from tkinter import filedialog as fdg
from matplotlib import pyplot as plt


window = tk.Tk()

window.title = "Draw"

path = tk.StringVar()

def otevri_soubor():
    global data
    data = [[],[]]
    path.set(fdg.askopenfilename())

    with open(path.get(), "r") as file: 
        for element in file:
            data[0].append(float(element.strip().split()[0]))
            data[1].append(float(element.strip().split()[1]))

def draw():
    plt.plot(data[0], data[1])
    plt.show()

path_etr = tk.Entry(window, textvariable=path)

path_etr.bind("<Return>", otevri_soubor)

open_btn = tk.Button(window, text="open file", command=otevri_soubor)

draw_btn = tk.Button(window, text="draw", command=draw)

path_etr.pack()

open_btn.pack()

draw_btn.pack()

tk.mainloop()