import math
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
x=np.linspace(0,1.0,num=10)
# original value of the derivative
y=[np.cos(math.pow(i,2))*2*i for i in x]
# forward difference approximation
z=[(np.sin(math.pow(i+0.01,2))-np.sin(math.pow(i,2)))/0.01 for i in x] # since h=0.01
# plotting the graph
ax.plot(x,y,"b",label="Actual value of the derivative")
ax.plot(x,z,"r",label="Forward finte difference approximation")
plt.grid(True,which="both")
plt.xticks(x)
ax.set_xlabel("x")
ax.set_ylabel("f'(x)")
ax.set_title('Plot of actual derivative and forward finite difference of $sin(x^2)$',fontsize=7.5)
ax.legend()
plt.show()