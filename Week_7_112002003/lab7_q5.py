import numpy as np
from numpy import cos, sin, pi, exp
import matplotlib.pyplot as plt
'''
The formula for newton-raphson for vector valued function is 
x_{k+1}= x_k -J(x_k)^{-1}*F(x_K)
we simplyfy it to 
(x_{k+1} -x_k)*J(x_k)=F(x_k) 
and hence to find x we solve the equation (DX)J(x_k)=F(x_k) with numpy.linalg
'''

def Newton_Raphson(F, J, x, eps):
    F_value = F(x)
    # to start the iteration
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    norm_values = []
    counter = []
    iteration_counter = 0
    # calculation for the norm
    while abs(F_norm) > eps:
        delta = np.linalg.solve(J(x), -F_value) # solving the linear equation as menioned before
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        norm_values.append(F_norm)
        iteration_counter += 1
        counter.append(iteration_counter)

    print("The solution vector is:", x)
    # plotting the convergence
    fig, ax = plt.subplots()
    ax.plot(counter, norm_values, "r--", label="Convergence of Newton-Raphson")
    ax.set_xlabel("No of iterations")
    ax.set_ylabel("Norm Values")
    ax.set_title("Plot of Norm values of f with respect to no of iterations", fontsize=10)
    ax.grid()
    ax.legend()

    plt.show()

# The given function
def Function(x):
    return np.array(
        [3 * x[0] - cos(x[1] * x[2]) - 3 / 2,
         4 * x[0] ** 2 - 625 * x[1] ** 2 + 2 * x[2] - 1, 20 * x[2] + exp(-x[0] * x[1]) + 9])

# jacobian for the given function
def Jacobian(x):
    return np.array(
        [[3, x[2] * sin(x[1] * x[2]), x[1] * sin(x[1] * x[2])],
         [8 * x[0], -1250 * x[1], 2], [-x[1] * exp(-x[1] * x[0]), -x[0] * exp(-x[1] * x[0]), 20]])


Newton_Raphson(Function, Jacobian, x=np.array([1, 2, 3]), eps=0.000001)