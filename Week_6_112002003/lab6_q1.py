import numpy as np
import matplotlib.pyplot as plt
from  scipy.interpolate import barycentric_interpolate
# calculation for Euler forward method
def EulerForward(h):
    if isinstance(h,str)==True:
        try:
           raise Exception("h needs to be a rational number")
        except Exception as inst:
            print(type(inst))
            print(inst)
    x0=0 # intial value of x
    y0=5 # initial value of y
    sol_x=[]
    sol_y=[]
    f=lambda x,y: -2*y # RHS of our ODE
   #Euler Formula
    while x0<=10:
        yn=y0+h*f(x0,y0)
        sol_x.append(x0)
        sol_y.append(y0)
        x0=x0+h
        y0=yn
    return sol_x,sol_y
h=[0.1, 0.5, 1, 2, 3]

fig,ax=plt.subplots(5,figsize=(8,18),sharex=True)

f=lambda x: 5*np.exp(-2*x) # Original solution

for i in range(len(h)):
        x = EulerForward(h[i])[0]
        y = EulerForward(h[i])[1]
        exact_y = [f(i) for i in x ] # exact values of y
        x_obs = np.linspace(min(x), max(x),150)
        y_obs = barycentric_interpolate(x, y, x_obs) # plotting the polynomial with barycentric_interpolate
        ax[i].plot(x_obs, y_obs,label="Predicted value")
        ax[i].plot(x,exact_y,label="exact value")
        ax[i].legend()
        ax[i].grid()
        ax[i].set_title("Forward Euler for step length "+str(h[i]),fontsize=10)




fig.tight_layout(pad=5.0)
plt.show()