import tkinter as tk
from tkinter import messagebox as msg
from matplotlib import pyplot as plt

data = [[],[]]

window = tk.Tk()

window.title = "Draw"

rows_x_cols = tk.BooleanVar()
title = tk.StringVar()
label_x = tk.StringVar()
label_y = tk.StringVar()
grid_yes_no = tk.BooleanVar()
line_style = tk.StringVar()
line_color = tk.StringVar()
point_marker = tk.StringVar()
                        
def draw():
    if len(data[0]) > 0 and len(data[1]) > 0:
        plt.plot(data[0], data[1], color=line_color.get(), linestyle = line_style.get(), marker=point_marker.get())
        plt.xlabel(label_x.get())
        plt.ylabel(label_y.get())
        plt.title(title.get())
        if grid_yes_no.get() == True:
            plt.grid()
        plt.show()
    else:
        msg.showwarning("Error", "No data to draw.\nPlease load a compatible .txt or .csv file!")

label = tk.Label(window, text="Vizualizace goniometrických funkcí")
label.grid(row=0, column=0)

param_frame = tk.LabelFrame(window, text="Parametry")

graph_frame = tk.LabelFrame(window, text="Vzhled")
graph_frame.grid(row=2, column=1)

draw_btn = tk.Button(graph_frame, text="Vykreslit", command=draw, width=16)
draw_btn.grid(row=4, column=1)

titulek = tk.Label(graph_frame, text="Nadpis")
titulek.grid(row=6, column=0)

title_etr = tk.Entry(graph_frame, textvariable=title)
title_etr.grid(row=6, column=1)

x_label = tk.Label(graph_frame, text="Popisek osy x")
x_label.grid(row=7, column=0)

x_etr = tk.Entry(graph_frame, textvariable=label_x)
x_etr.grid(row=7, column=1)

y_label = tk.Label(graph_frame, text="Popisek osy y")
y_label.grid(row=8, column=0)

y_etr = tk.Entry(graph_frame, textvariable=label_y)
y_etr.grid(row=8, column=1)

grid_label = tk.Label(graph_frame, text="Mřížka")
grid_label.grid(row=9, column=0)

grid_yes_no.set(True)
grid = tk.Checkbutton(graph_frame, variable=grid_yes_no)
grid.grid(row=9, column=1, sticky="w")

line_style_label = tk.Label(graph_frame, text="Styl čáry")
line_style_label.grid(row=10, column=0)

line_style.set("-")
line_style_menu = tk.OptionMenu(graph_frame, line_style, "-", "--", ":", "-.")
line_style_menu.grid(row=10, column=1, sticky="w")

line_color_label = tk.Label(graph_frame, text="Line color")
line_color_label.grid(row=11, column=0)

line_color.set("blue")
line_color_menu = tk.OptionMenu(graph_frame, line_color, "red", "green", "blue", "cyan", "magenta", "yellow", "black")
line_color_menu.grid(row=11, column=1, sticky="w")

marker_label = tk.Label(graph_frame, text="Znak bodu")
marker_label.grid(row=12, column=0)

point_marker.set(",")
marker_menu = tk.OptionMenu(graph_frame, point_marker, ".", ",", "o", "^", "s", "P")
marker_menu.grid(row=12, column=1, sticky="w")




tk.mainloop()