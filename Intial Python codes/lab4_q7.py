import numpy as np
import math


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

    def derivative(self):
        derivative_list = []
        for i in range(1, len(self.list_co)):
            derivative_list.append((i) * self.list_co[i])
        self.list_co = derivative_list
        return self

    def area(self, a, b):
        self.a = a
        self.b = b
        Integration_list = [0]
        for i in range(len(self.list_co)):
            Integration_list.append(self.list_co[i] / (i + 1))
        p = Polynomial(Integration_list)
        return "Area in the interval " + str([self.a, self.b]) + " is: " + str((p[self.b] - p[self.a]))


# Approximate the integration with taylor series polynomial
fn = lambda n: 2 ** (n / 2) * np.sin(n * np.pi / 4)  # nth order derivative of the function e^x sin(x) at x=0
x = [fn(i) / math.factorial(i) for i in range(7)]  # Initializing the taylor polynomial up to  x^7
p = Polynomial(x)  # creating the polynomial
print(p.area(0, 1 / 2))  # calculating the area/integration with our area method
