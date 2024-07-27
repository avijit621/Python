import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from scipy.special import gamma
''''
#x=math.log(math.factorial(5))
#y=math.log(math.sqrt(2*np.pi*(5))) + 5 *(math.log(5)-math.log(np.e))

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [])

def init():
    ax.set_xlim(0, 5)
    ax.set_ylim(6,120)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(math.factorial(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=10,
                    init_func=init, blit=True)
plt.show()
'''
print(gamma(7))