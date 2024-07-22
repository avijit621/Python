import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# Fourier approximation of nth degree for the  function e^x
def FourierApproximation(degree):
    a = []
    b = []

    for i in range(degree + 1):
        s = lambda x: np.exp(x) * np.cos(i * x)  # calculation for ak
        r = lambda x: np.exp(x) * np.sin(i * x)  # calculation of bk
        a.append((1 / np.pi) * list(integrate.quad(s, -np.pi, np.pi))[0])  # storing ak values
        b.append((1 / np.pi) * list(integrate.quad(r, -np.pi, np.pi))[0])  # stroring bk values
    # printing the co-effecients ak and bk
    print("The co-effecients are as follows:")
    print("co-effecients of cosines are ", a)
    print("co-effecients of sines are ", b)
    x = np.linspace(-np.pi, np.pi, num=1000)
    s = a[0] / 2 # since the 1st term in fourier series is a_0/2
    sn = []
    # calculation of S_n(x) for all x
    for i in x:
        for j in range(1, degree + 1):
            s = s + a[j] * np.cos(i * j) + b[j] * np.sin(j * i)
        sn.append(s)
        s = a[0] / 2
    fig, ax = plt.subplots()
    y = [np.exp(i) for i in x]
    ax.plot(x, y, label="$e^x$")
    ax.plot(x, sn, label="Fourier approximation")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Fourier approximation vs actual plot of $e^x$")
    plt.grid(True, which="both")
    ax.legend()
    plt.show()


FourierApproximation(20)
