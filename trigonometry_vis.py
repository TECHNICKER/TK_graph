import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

y_value = []
x_time = []

window = tk.Tk()

a = 5          #amplituda    
b = 1          #periodicita
c = 3          #fázový posun -4 až 4
d = 0          #vertikální posun

for x in np.arange(-100, 100, 2*np.pi/1000):
       y = a * np.sin((b*x) + (c*(1/2*np.pi))) + d                  #sine
       # y = a * np.cos((b*x) + (c*(1/2*np.pi))) + d                  #cosine
       # y = a * np.tan((b*x) + (c*(1/2*np.pi))) + d                  #tan
       # y = a * ((np.cos(b*x)) / (np.sin(b*x))) + d                  #cotan        fix-fáze
       # y = a * np.arcsin((b*x) + (c*(1/2*np.pi))) + d               #arc-sine     fix-periodicita, faze, posun
       # y = a * np.arccos((b*x) + (c*(1/2*np.pi))) + d               #arc-cos      fix-periodicita, faze, posun
       # y = a * np.arctan((b*x) + (c*(1/2*np.pi))) + d               #arc-tan
       # y = a * (1 / (np.cos(b*x))) + d                              #sec          fix-fáze     
       # y = a * (1 / (np.sin(b*x))) + d                              #csc          fix-fáze


       y_value.append(y)
       x_time.append(x)

fig, ax = plt.subplots()
ax.plot(x_time, y_value)

ax.set(xlabel='time [s]', ylabel='value [-]',
       title='vybrana funkce')
ax.grid(visible=None, which="major", axis="y")

# plt.ylim(-50, +50)
# plt.xlim(-10, 10)
# plt.grid(color = "#d9d9d9")
# plt.axhline(color = "red", linestyle = "dashed" )
# plt.axvline(color = "red", linestyle = "dashed")
# plt.axvline(2*np.pi/np.abs(b), color = "black", linestyle = "dotted")
# plt.show()




tk.mainloop()