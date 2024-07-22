import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
h = np.linspace(0.001, 0.01, 100)
x = np.linspace(0, 1, 100)
FD_max_err_list = []
CD_max_err_list = []
# print(x)
for i in h:
    # for each i calculating all the error values for forward difference
    err_list1 = [abs(np.cos(j ** 2) * 2 * j - (np.sin((j + i) ** 2) - np.sin(j ** 2)) / i) for j in x]
    # for each i calculating all the error values for centered  difference
    err_list2 = [abs(np.cos(j ** 2) * 2 * j- (np.sin(math.pow(j + i, 2)) - np.sin(math.pow(j - i, 2))) / (2 * i) )  for j in x]
    # Getting the max error
    max_err1 = max(err_list1)
    max_err2=max(err_list2)
    # creating a list of max errors
    FD_max_err_list.append(max_err1)
    CD_max_err_list.append(max_err2)
    err_list1.clear()
    err_list2.clear()
# plotting the values
ax.plot(h, FD_max_err_list,"r",label="Forward difference")
ax.plot(h,CD_max_err_list,"b",label="Centred Difference")
plt.grid(True, which="both")
ax.set_xlabel("h")
ax.set_ylabel("Maximum Error")
ax.set_title("Plot of maximum error for different values of h")
ax.legend()
plt.show()


