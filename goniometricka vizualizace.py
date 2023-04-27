import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt

window = tk.Tk()
window.title("Vizualizace goniometrických funkcí")

rows_x_cols = tk.BooleanVar()
title = tk.StringVar()
label_x = tk.StringVar()
label_y = tk.StringVar()
grid_yes_no = tk.BooleanVar()
live_mode = tk.BooleanVar()
line_style = tk.StringVar()
line_color = tk.StringVar()
point_marker = tk.StringVar()

funkce = tk.IntVar()

ampl = tk.IntVar()
freq = tk.IntVar()
faze = tk.IntVar()
posun = tk.IntVar()
                        
def draw(*args, **kwargs):
    if live_mode.get() == 1 or "redraw" in args:
        data = [[],[]]

        plt.clf()
        if funkce.get() == 0:
            for x in np.arange(-10, 10, 2*np.pi/1000):
                y = ampl.get() * np.sin((freq.get()*x) + ((faze.get()/2)*np.pi)) + posun.get() 

                data[0].append(x)
                data[1].append(y)

        elif funkce.get() == 1:
            for x in np.arange(-10, 10, 2*np.pi/1000):
                y = ampl.get() * np.cos((freq.get()*x) + ((faze.get()/2)*np.pi)) + posun.get() 

                data[0].append(x)
                data[1].append(y)

        elif funkce.get() == 2:
            for x in np.arange(-10, 10, 2*np.pi/10000):
                y = ampl.get() * np.tan((freq.get()*x) + ((faze.get()/2)*np.pi)) + posun.get() 

                data[0].append(x)
                data[1].append(y)
        
        plt.plot(data[0], data[1], color=line_color.get(), linestyle = line_style.get(), marker=point_marker.get())
        plt.ylim(-50, +50)
        plt.xlim(-10, 10)
        plt.axhline(color = "red", linestyle = "dashed" )
        plt.axvline(color = "red", linestyle = "dashed")
        if freq.get() != 0:
            period = 2*np.pi/np.abs(freq.get())
            ticks = []
            plt.axvline(period, color = "black", linestyle = "dotted")
            for i in np.arange(-10, 11, 2.5):
                if np.isclose(i, period, 0.55) == False:
                    ticks.append(i)

            ticks.append(period)

            plt.xticks(ticks)

        plt.xlabel(label_x.get())
        plt.ylabel(label_y.get())
        plt.title(title.get())
        if grid_yes_no.get() == True:
            plt.grid(color = "#d9d9d9")
        plt.show()

param_frame = tk.LabelFrame(window, text="Parametry", height=270, width=177)
param_frame.grid_propagate(False)
param_frame.grid(row=2, column=1)


live = tk.Checkbutton(param_frame, variable=live_mode)
live.grid(row=1, column=2, sticky="E")

sin_button = tk.Radiobutton(param_frame, text="sinus", variable=funkce, value=0, command=draw)
sin_button.grid(row=0, column=0, sticky="W")

cos_button = tk.Radiobutton(param_frame, text="cosinus       real time:", variable=funkce, value=1, command=draw)
cos_button.grid(row=1, column=0, sticky="W")

tan_button = tk.Radiobutton(param_frame, text="tangens", variable=funkce, value=2, command=draw)
tan_button.grid(row=2, column=0, sticky="W")


ampl_label = tk.Label(param_frame, text="Amplituda [ - ]")
ampl_label.grid(row=3, column=0, sticky="E")

freq_label = tk.Label(param_frame, text="Frekvence [Hz]")
freq_label.grid(row=5, column=0, sticky="E")

faze_label = tk.Label(param_frame, text="Fázový posun [π/2]")
faze_label.grid(row=7, column=0, sticky="E")

posun_label = tk.Label(param_frame, text="Vertikální posuv [ - ]")
posun_label.grid(row=9, column=0, sticky="E")


ampl_entry = tk.Entry(param_frame, textvariable=ampl, width=4)
ampl_entry.grid(row=4, column=2)

freq_entry = tk.Entry(param_frame, textvariable=freq, width=4)
freq_entry.grid(row=6, column=2)

faze_entry = tk.Entry(param_frame, textvariable=faze, width=4)
faze_entry.grid(row=8, column=2)

posun_entry = tk.Entry(param_frame, textvariable=posun, width=4)
posun_entry.grid(row=10, column=2)


ampl_scale = tk.Scale(param_frame, from_=0, to=100, orient="horizontal", showvalue=False, variable=ampl, length=130, command=draw)
ampl_scale.grid(row=4, column=0, columnspan=2)

freq_scale = tk.Scale(param_frame, from_=0, to=20, orient="horizontal", showvalue=False, variable=freq, length=130, command=draw)
freq_scale.grid(row=6, column=0, columnspan=2)

faze_scale = tk.Scale(param_frame, from_=-4, to=4, orient="horizontal", showvalue=False, variable=faze, length=130, command=draw)
faze_scale.grid(row=8, column=0, columnspan=2)

posun_scale = tk.Scale(param_frame, from_=-100, to=100, orient="horizontal", showvalue=False, variable=posun, length=130, command=draw)
posun_scale.grid(row=10, column=0, columnspan=2)


graph_frame = tk.LabelFrame(window, text="Vzhled", height=270, width=177)
graph_frame.grid_propagate(False)
graph_frame.grid(row=2, column=0)

draw_btn = tk.Button(graph_frame, text="Vykreslit", command=lambda: draw("redraw"), width=11)
draw_btn.grid(row=4, column=1, sticky="W")

titulek = tk.Label(graph_frame, text="Nadpis")
titulek.grid(row=6, column=0, sticky="E")

title_etr = tk.Entry(graph_frame, textvariable=title, width=14)
title_etr.grid(row=6, column=1, sticky="W")
title_etr.bind("<Return>", draw)

x_label = tk.Label(graph_frame, text="Popisek osy x")
x_label.grid(row=7, column=0, sticky="E")

x_etr = tk.Entry(graph_frame, textvariable=label_x, width=14)
x_etr.grid(row=7, column=1, sticky="W")
x_etr.bind("<Return>", draw)

y_label = tk.Label(graph_frame, text="Popisek osy y")
y_label.grid(row=8, column=0, sticky="E")

y_etr = tk.Entry(graph_frame, textvariable=label_y, width=14)
y_etr.grid(row=8, column=1, sticky="W")
y_etr.bind("<Return>", draw)

grid_label = tk.Label(graph_frame, text="Mřížka")
grid_label.grid(row=9, column=0, sticky="E")

grid_yes_no.set(True)
grid = tk.Checkbutton(graph_frame, variable=grid_yes_no, command=draw)
grid.grid(row=9, column=1, sticky="W")

line_style_label = tk.Label(graph_frame, text="Styl čáry")
line_style_label.grid(row=10, column=0, sticky="E")

line_style.set("-")
line_style_menu = tk.OptionMenu(graph_frame, line_style, "-", "--", ":", "-.", command=draw)
line_style_menu.grid(row=10, column=1, sticky="W")

line_color_label = tk.Label(graph_frame, text="Barva čáry")
line_color_label.grid(row=11, column=0, sticky="E")

line_color.set("blue")
line_color_menu = tk.OptionMenu(graph_frame, line_color, "red", "green", "blue", "cyan", "magenta", "yellow", "black", command=draw)
line_color_menu.grid(row=11, column=1, sticky="W")

marker_label = tk.Label(graph_frame, text="Znak bodu")
marker_label.grid(row=12, column=0)

point_marker.set(",")
marker_menu = tk.OptionMenu(graph_frame, point_marker, ".", ",", "o", "^", "s", "P", command=draw)
marker_menu.grid(row=12, column=1, sticky="W")




tk.mainloop()