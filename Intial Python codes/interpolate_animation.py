

from scipy import interpolate
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.animation as ani

def animate(values):

    x=np.linspace(0,1,values)
    y=[np.tan(i)*np.sin(30*i)*(np.e**i) for i in x ]

    #y1=[math.tan(i)*math.sin(30*i)*(math.e**i) for i in x1]
    #for i in range(len(x1)):
     #   tmp=x1[i]
      #  tmp1=math.tan(tmp)*math.sin(30*tmp)*(math.e**tmp)
       # y1.append(tmp1)
    arr = np.arange(0, 1.1, 0.01)
    s = interpolate.CubicSpline(x1, y1)
    t=interpolate.Akima1DInterpolator(x1,y1)
    f=interpolate.BarycentricInterpolator(x1,y1)
    sline.set_ydata(s(arr))
    sline.set_xdata(arr)
    fline.set_ydata(f(arr))
    fline.set_xdata(arr)
    tline.set_ydata(t(arr))
    tline.set_xdata(arr)
    plt.title("Different interpolations of "+r'$tan(x) \cdot sin(30x) \cdot e^x$ for '+str(samples)+" samples")
    return sline,tline,fline

x=[]
y=[]
i=0
while i<=1:
    tmp=math.tan(i)*math.sin(30*i)*(math.e**i)
    x.append(i)
    y.append(tmp)
    i+=0.01
fig,ax= plt.subplots()
fontP = FontProperties()
fontP.set_size('xx-small')
plt.plot(x, y, 'b-',label="True")
plt.xlabel(r'$x$')
plt.ylabel(r'$\bar{f(x)}$')
plt.grid(True)
plt.xlim([0,1])
plt.ylim([-4,4])

sline,=plt.plot(0,0, 'r-', label='Cubic Spline')
tline,=plt.plot(0,0, 'g-', label='Akima')
fline,=plt.plot(0,0, 'm-', label='Barycentric')
plt.legend(loc='upper left')

l=[i for i in range(2,36,1)]
animator = ani.FuncAnimation(fig, animate,l, interval = 300,repeat=False,blit=False)
plt.show()

