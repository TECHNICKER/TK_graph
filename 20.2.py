import tkinter as tk
from tkinter import filedialog as fdg
from matplotlib import pyplot as plt


window = tk.Tk()

window.title = "Draw"

path = tk.StringVar()
rows_x_cols = tk.BooleanVar()
title = tk.StringVar()
label_x = tk.StringVar()
label_y = tk.StringVar()
grid_yes_no = tk.BooleanVar()
line_style = tk.StringVar()
line_color = tk.StringVar()
point_marker = tk.StringVar()


def otevri_soubor():
    global data
    data = [[],[]]
    path.set(fdg.askopenfilename())

    with open(path.get(), "r") as file: 
        if path.get()[-4:] == ".txt":
            for element in file:
                data[0].append(float(element.strip().split()[0]))
                data[1].append(float(element.strip().split()[1]))

        elif path.get()[-4:] == ".csv":
            for element in file:
                for pair in element.split(","):
                    if len(pair.split(";")) == 2:
                        data[0].append(float(pair.split(";")[0]))
                        data[1].append(float(pair.split(";")[1]))


def draw():
    plt.plot(data[0], data[1], color=line_color.get(), linestyle = line_style.get(), marker=point_marker.get())
    plt.xlabel(label_x.get())
    plt.ylabel(label_y.get())
    plt.title(title.get())
    if grid_yes_no.get() == True:
        plt.grid()
    plt.show()

label = tk.Label(window, text="Tk_Graph")
label.grid(row=0, column=0)

file_frame = tk.LabelFrame(window, text="File")
file_frame.grid(row=1, column=0)

path_etr = tk.Entry(file_frame, textvariable=path)
path_etr.grid(row=2, column=0)

path_etr.bind("<Return>", otevri_soubor)

open_btn = tk.Button(file_frame, text="...", command=otevri_soubor)
open_btn.grid(row=2, column=1)

draw_btn = tk.Button(file_frame, text="draw", command=draw)
draw_btn.grid(row=4, column=1)

radky = tk.Radiobutton(file_frame, text="Data in rows", variable=rows_x_cols, value=0)
sloupce = tk.Radiobutton(file_frame, text="Data in columns", variable=rows_x_cols, value=1)
radky.grid(row=3, column=0, sticky="w")
sloupce.grid(row=4, column=0, sticky="w")


graph_frame = tk.LabelFrame(window, text="Graph")
graph_frame.grid(row=5, column=0)

titulek = tk.Label(graph_frame, text="Title")
titulek.grid(row=6, column=0)

title_etr = tk.Entry(graph_frame, textvariable=title)
title_etr.grid(row=6, column=1)

x_label = tk.Label(graph_frame, text="X label")
x_label.grid(row=7, column=0)

x_etr = tk.Entry(graph_frame, textvariable=label_x)
x_etr.grid(row=7, column=1)

y_label = tk.Label(graph_frame, text="Y label")
y_label.grid(row=8, column=0)

y_etr = tk.Entry(graph_frame, textvariable=label_y)
y_etr.grid(row=8, column=1)

grid_label = tk.Label(graph_frame, text="Grid")
grid_label.grid(row=9, column=0)

grid_yes_no.set(True)
grid = tk.Checkbutton(graph_frame, variable=grid_yes_no)
grid.grid(row=9, column=1, sticky="w")

line_style_label = tk.Label(graph_frame, text="Line style")
line_style_label.grid(row=10, column=0)

line_style.set("-")
line_style_menu = tk.OptionMenu(graph_frame, line_style, "-", "--", ":", "-.")
line_style_menu.grid(row=10, column=1, sticky="w")

line_color_label = tk.Label(graph_frame, text="Line color")
line_color_label.grid(row=11, column=0)

line_color.set("blue")
line_color_menu = tk.OptionMenu(graph_frame, line_color, "red", "green", "blue", "cyan", "magenta", "yellow", "black")
line_color_menu.grid(row=11, column=1, sticky="w")

marker_label = tk.Label(graph_frame, text="Marker")
marker_label.grid(row=12, column=0)

point_marker.set(",")
marker_menu = tk.OptionMenu(graph_frame, point_marker, ".", ",", "o", "^", "s", "P")
marker_menu.grid(row=12, column=1, sticky="w")




tk.mainloop()