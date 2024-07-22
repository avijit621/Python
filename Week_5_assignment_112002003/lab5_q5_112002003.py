import matplotlib.pyplot as plt
import numpy as np


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


# creating the n th degree chebyshev polynomial
def ChebyshevPolynomial(degree):
    p1 = Polynomial([1]) # 1st chebyshev polynomial
    p2 = Polynomial([0, 1]) # 2nd chebyshev polynomial
    i = 1
    # recursive calculation for chebyshev's polynomial with T_(n+1)(x)=2xT_n(x) - T_(n-1)(x)
    while i < degree:
        p = 2 * Polynomial([0, 1]) * p2 - p1
        p1 = p2
        p2 = p
        i += 1
    if degree == 0:
        print(p1)
    elif degree == 1:
        print(p2)
    else:
        print(p)


ChebyshevPolynomial(11)
