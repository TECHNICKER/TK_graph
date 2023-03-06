from numpy import linspace as ls
from matplotlib import pyplot as plt
from scipy import interpolate as interp


x = "0 0.3 0.5 0.8 1 2 3".split()
y = "0 0.1 0.5 1 3 10 30".split()

x = list(map(float, x))
y = list(map(float, y))

newx = ls(0, 3, 50)
spl = interp.UnivariateSpline(x, y)
newy = spl(newx)

plt.plot(newx, newy, linestyle = ":", label = "interpolation")
plt.plot(x, y, "o", label = "měřící body")
plt.show()

# spline = interpolate.CubicSpline(x, y)