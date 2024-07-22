import numpy as np
import matplotlib.pyplot as plt


def CompareConvergence():
    f = lambda x: x - np.cos(x)  # function f
    df = lambda x: 1 + np.sin(x)  # derivative of f
    # Calculation by secant method
    x0 = 0
    x1 = 5
    h = 0
    secant_value = []
    secant_counter = []
    while abs(f(x1)) > 10 ** (-10):  # error threshold is 10^-10
        if (f(x1) - f(x0) != 0):
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            x0 = x1
            x1 = x2
            h = h + 1
            secant_counter.append(h)
            secant_value.append(f(x2))

    # calculation by Newton Raphson method
    k = 0
    x0 = 1
    newton_value = []
    newton_counter = []
    while abs(f(x0)) > 10 ** (-10):
        h = f(x0) / df(x0)
        xk = x0 - h
        x0 = xk
        k = k + 1
        newton_counter.append(k)
        newton_value.append(f(x0))
        # print(x0)
    fig, ax = plt.subplots()
    ax.plot(newton_counter, newton_value, "r-", label="Newton raphson")
    ax.plot(secant_counter, secant_value, "b--", label="Secant Method")
    ax.grid()
    ax.legend()
    ax.set_xlabel("No of iterations")
    ax.set_ylabel("functional Values")
    ax.set_title("Convergence of Newton-Raphson vs Secant Method", fontsize=10)
    plt.show()


CompareConvergence()