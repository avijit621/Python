import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt
import matplotlib.animation

def update(values):
    x=np.linspace(0,1,values)
    y=[np.tan(i)*np.sin(30*i)*(np.e**i) for i in x]
    xnew= np.arange(0, 1.1, 0.01)
    f1=interpolate.interp1d(x,y,)
    f2=interpolate.interp1d(x,y)
    f3=interpolate.interp1d(x,y,)
    sline.set_ydata(f1(xnew))

    return f1,f2,f3
x= np.arange(0,1,0.01)
y=[np.tan(i)*np.sin(30*i)*(np.e**i) for i in x]
fig,ax= plt.subplots()
plt.grid(True)
plt.xlim([0,1])
plt.ylim([-4,4])
f1=plt.plot(0,0)
f2=plt.plot(0,0)
f3=plt.plot(0,0)
l=[i for i in range(2,36,1)]
animator = matplotlib.animation.FuncAnimation(fig, update,l, interval = 300,repeat=False,blit=False)
plt.show()
