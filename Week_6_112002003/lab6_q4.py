import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# the function takes arguments mu and initial condition x(0)=1 and x'(0)=0 as (0,1) and (0,0) respectively
def vanderpol(mu, x0, dx0):  # x0 and y0 are the intitial conditions
    if isinstance(mu, str) == True or mu <0:
        try:
            raise Exception("The parameter needs to be a positive real number")
        except Exception as inst:
            print(type(inst))
            print(inst)
        return None
    # function returning van der pol equation
    def f(t, z):
        x, y = z
        return [y, mu * (1 - x ** 2) * y - x]

    # function for calculating time period
    def root(t, y):
        return y[0]

    a, b = 0, 10
    t = np.linspace(a, b, 500)
    fig, ax = plt.subplots(2)
    # solution for plotting using solve_ivp
    sol = solve_ivp(f, [a, b], [x0[1], dx0[1]], t_eval=t)
    ax[0].plot(sol.y[0], sol.y[1], "--", label="$\mu=$" + str(mu))  # plotting phase protraits
    ax[1].plot(sol.t, sol.y[0], "r-", label="$\mu=$" + str(mu))  # plot with respect to time
   # solution for time period
    sol1 = solve_ivp(f, [0, 40], [1, 0], events=root)
    # find the zeros of the solution over the interval [a, b]
    zeroes = sol1.t_events[0]
    # To estimate the period of the limit cycle we look at the spacing between zeros
    l = len(zeroes)
    print("The time period is ", 2*(zeroes[l - 1] - zeroes[l - 2])) # e find the half period in the previous step
                                                                    # hence time period is twice of that
    ax[0].set_xlim([-3, 3])
    ax[0].set_title("Plot of  phase portrait",fontsize=10)
    ax[1].set_title("Plot with respect to time ",fontsize=10)
    ax[0].legend()
    ax[1].legend()
    fig.tight_layout(pad=3.0)
    plt.show()



vanderpol(2, (0, 1), (0, 0))
