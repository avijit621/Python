import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
I_trapz_list=[]
I_simps_list=[]
I_quad_list=[]
I_real_list=[]
# function we nned to find the area under
f= lambda x: 2*x*np.exp(x**2)
u=np.linspace(0,3,200) # divide the interval (0,3) into sub-intervals  (0,u)
for i in range(1,len(u)):
   I_quad=scipy.integrate.quad(f,0,u[i])
   x=np.linspace(0,u[i],100) # array to use in trapezoid and simpson
   y=f(x)
   I_trapz=scipy.integrate.trapz(y,x)

   I_simps=scipy.integrate.simps(y,x)
   I_real_list.append(np.exp(u[i]**2)-np.exp(1)) # original value of the integration
   I_trapz_list.append(I_trapz) # trapezoidal approximation
   I_simps_list.append(I_simps) # simpson's approximation
   I_quad_list.append(I_quad[0]) # Quadrature rule
x=[u[i] for i in range(1,len(u))] # x axis values
# plot of the function
fig,ax=plt.subplots()
ax.plot(x,I_simps_list,"y^",label="Simpson's Rule")
ax.plot(x,I_quad_list,"r",label="Quadrature")
ax.plot(x,I_trapz_list,":",linewidth=5,label="Trapezoidal Rule")
ax.plot(x,I_real_list,"g--",label="Real value")
ax.legend()
ax.set_xlabel("End point of the interval ")
ax.set_ylabel("Value of the integration")
plt.grid(True,which="both")
ax.set_title("Plot of different Numerical integration methods in scipy",fontsize=12)
plt.show()