import math
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
x=np.linspace(0,1.0,num=10)
# original value of the derivative
y=[np.cos(math.pow(i,2))*2*i for i in x]
# Forward difference approximation
FD=[(np.sin(math.pow(i+0.01,2))-np.sin(math.pow(i,2)))/0.01 for i in x]
# backward difference approximation
BD=[(np.sin(math.pow(i,2))-np.sin(math.pow(i-0.01,2)))/0.01 for i in x]
# Centered difference approximation
CD=[(np.sin(math.pow(i+0.01,2))-np.sin(math.pow(i-0.01,2)))/(2*0.01) for i in x]
# error for FD,CD,BD
err_FD=[abs(y[i]-FD[i]) for i in range(len(x))]
err_BD=[abs(y[i]-BD[i]) for i in range(len(x))]
err_CD=[abs(y[i]-CD[i]) for i in range(len(x))]
# plotting of values
ax.plot(x,err_CD,"g",label="Forward Difference")
ax.plot(x,err_FD,"r",label="Centered difference")
ax.plot(x,err_BD,"b",label="Backward difference")
ax.set_xlabel("x")
ax.set_ylabel("Error in estimation")
ax.set_title("Plot of Error Estimation in Numerical Differentiation")
plt.grid(True,which="both")
ax.legend()
plt.show()