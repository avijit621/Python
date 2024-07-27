import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
M = 500 # setting the max value of M
I_trap = []
I = 0
x = 1
for i in range(2, M + 1):
    x = 1
    h = 2 / i # h is set for each M
    while x+h <= 3:
        # calculation of sum in the trapezoidal value
        I = I + ((2*x*np.e**(x**2))+(2*(x+h)*np.e**((x+h)**2)))/2

        x = x + h
    I_trap.append(h *I)
    I = 0
# setting x_axis values
x = np.linspace(2, M, M-1)
# plotting the values
ax.plot(x, I_trap,label=" Estimate of area by Trapezoidal rule")
plt.grid(True, which="both")
plt.axhline(y=np.e ** 9 - np.e,color="r",label="Actual Area")
ax.set_ylim([min(I_trap),max(I_trap)])
ax.set_xlabel("No of intervals",fontsize=10)
ax.set_ylabel("Area",fontsize=10)
ax.set_title("Area under the curve $2xe^{x^2}$",fontsize=10)
ax.legend()
plt.show()

