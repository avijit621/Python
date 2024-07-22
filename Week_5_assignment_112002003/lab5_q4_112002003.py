import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate


class Polynomial:
    def __init__(self, list_co=[]):
        self.list_co = list_co

    def __str__(self):
        strings = []
        strings.append("Coefficients of the polynomial are:")
        temp = " ".join([str(x) for x in self.list_co])
        strings.append(str(temp))
        return "\n".join(strings)

    # Evaluating the polynomial at a point and using getitem to hget the value
    def __getitem__(self, item):
        return sum([(item ** i) * self.list_co[i] for i in range(len(self.list_co))])

    # Defining addition of Polynom,ials properly
    def __add__(self, other):
        size = max(len(self.list_co), len(other.list_co))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.list_co), 1):
            sum[i] = self.list_co[i]
        for i in range(len(other.list_co)):
            sum[i] += other.list_co[i]
        self.list_co = sum
        return self

    # defining Subtraction properly
    def __sub__(self, other):
        size = max(len(self.list_co), len(other.list_co))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.list_co), 1):
            sum[i] = self.list_co[i]
        for i in range(len(other.list_co)):
            sum[i] -= other.list_co[i]
        self.list_co = sum
        return self

    # Defining constant multiplication
    def __rmul__(self, other):
        vector = self.list_co
        for i in range(len(vector)):
            self.list_co[i] = other * self.list_co[i]
        return self

    # defining multiplication of two ploynomials
    def __mul__(self, other):
        r1 = len(self.list_co)
        r2 = len(other.list_co)
        prod = [0] * (r1 + r2 - 1)
        for i in range(r1):
            for j in range(r2):
                prod[i + j] += self.list_co[i] * other.list_co[j]
        self.list_co = prod
        return self

    def derivative(self):  # derivative method
        derivative_list = []
        for i in range(1, len(self.list_co)):
            # The derivative formula of the polynomial [x^n becomes x^(n-1)]
            derivative_list.append((i) * self.list_co[i])
        self.list_co = derivative_list
        return self

    def area(self, a, b):  # area method
        self.a = a
        self.b = b
        # intilalizing the list of the co-efficients with a zero to compensate for the constant in integration
        Integration_list = [0]
        for i in range(len(self.list_co)):
            # integration formula of a polynomial [x^n becomes  x^n/n+1]
            Integration_list.append(self.list_co[i] / (i + 1))
        p = Polynomial(Integration_list)  # Creating a polynomial with the co-efficients
        return "Area in the interval " + str([self.a, self.b]) + " is: " + str((p[self.b] - p[self.a]))

    def LegendrePolynomial(self, degree): # method for evaluating legendre polynomial
        p = Polynomial([-1, 0, 1])
        s = Polynomial([1])
        for i in range(degree):
            s = s * p

        for i in range(degree):
            s = s.derivative()

        l = (1 / ((2 ** degree) * math.factorial(degree))) * s

        return l

    def legend_approximation(self, degree): # the method to approximate using nth degree legendre polynomial
        p = Polynomial()
        aj = []
        for i in range(degree + 1):
            # calculation of cj starts with weight function w(x)=1
            s = lambda x: p.LegendrePolynomial(i).legendre_function(x) ** 2
            # calculation of aj
            r = lambda x: p.LegendrePolynomial(i).legendre_function(x) * np.exp(x)
            # cj values
            cj = list(integrate.quad(s, -1, 1))[0]
            # calculating the co-effecients i.e. aj
            tmp = (1 / cj) * list(integrate.quad(r, -1, 1))[0]
            aj.append(tmp) # creating a list of co-effecients
        # estimating the polynomial
        p_leg = Polynomial([0])
        for i in range(degree + 1):
            p_leg = p_leg + aj[i] * p.LegendrePolynomial(i)
        print(p_leg)
        a = -1
        b = 1

        x = np.linspace(a, b, num=1000)
        # setting up a polynomial object to valuate a value at points and
        # using it in a plot
        y = [p_leg[i] for i in x]
        z = [np.exp(i) for i in x]
        fig, ax = plt.subplots()

        ax.plot(x, z, 'yo', label="$e^x$")
        ax.plot(x, y, 'b', label="Legendre fit")

        #ax.set_ylim([min(y), max(y)])
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.set_title("Legendre Polynomial fit vs actual plot of $e^x$")
        #ax.set_xlim(a, b)
        ax.legend()
        plt.grid(True, which="both")
        plt.show()

    # to return the polynomial object as powers of x (e.g [1,1,1] as 1+1*x+1*x^2)
    def legendre_function(self, x):
        s = 0
        for i in range(len(self.list_co)):
            s += (x ** i) * self.list_co[i]
        return s


p = Polynomial()
# p1=p.LegendrePolynomial(5)
p.legend_approximation(15)
