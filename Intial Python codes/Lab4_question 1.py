import matplotlib.pyplot as plt
import numpy  as np

fig,ax=plt.subplots()
x=np.arange(0,1+0.25,0.25)

y = [np.cos(i*2)*2*i for i in x ]
ax.set_ylim([0,2])
z=[ (np.sin((i+0.01)**2)-np.sin(i**2))/0.01 for i in x]
#ax.plot(x,y)
ax.plot(x,z,"r")
plt.grid(True,which="both")
#xnew = np.linspace(x.min(), x.max(), 300)

#spl = make_interp_spline(x, y, k=3)  # type: BSpline
#y_smooth = spl(xnew)

#plt.plot(xnew, y_smooth)
plt.show()
plt.show()
