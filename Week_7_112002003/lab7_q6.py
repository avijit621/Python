import numpy as np
import random


class Polynomial:
    def __init__(self, coef_co=[]):
        self.coef_co = coef_co

    def __str__(self):
        strings = []
        strings.append("Coefficients of the polynomial are:")
        temp = " ".join([str(x) for x in self.coef_co])
        strings.append(str(temp))
        return "\n".join(strings)

    # Evaluating the polynomial at a point and using getitem to hget the value
    def __getitem__(self, item):
        return sum([(item ** i) * self.coef_co[i] for i in range(len(self.coef_co))])

    # Defining addition of Polynom,ials properly
    def __add__(self, other):
        size = max(len(self.coef_co), len(other.coef_co))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.coef_co), 1):
            sum[i] = self.coef_co[i]
        for i in range(len(other.coef_co)):
            sum[i] += other.coef_co[i]
        self.coef_co = sum
        return self

    # defining Subtraction properly
    def __sub__(self, other):
        size = max(len(self.coef_co), len(other.coef_co))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.coef_co), 1):
            sum[i] = self.coef_co[i]
        for i in range(len(other.coef_co)):
            sum[i] -= other.coef_co[i]
        self.coef_co = sum
        return self

    # Defining constant multiplication
    def __rmul__(self, other):
        vector = self.coef_co
        for i in range(len(vector)):
            self.coef_co[i] = other * self.coef_co[i]
        return self

    # defining multiplication of two ploynomials
    def __mul__(self, other):
        r1 = len(self.coef_co)
        r2 = len(other.coef_co)
        prod = [0] * (r1 + r2 - 1)
        for i in range(r1):
            for j in range(r2):
                prod[i + j] += self.coef_co[i] * other.coef_co[j]
        self.coef_co = prod
        return self

    def derivative(self):  # derivative method
        derivative_coef = []
        for i in range(1, len(self.coef_co)):
            # The derivative formula of the polynomial [x^n becomes x^(n-1)]
            derivative_coef.append((i) * self.coef_co[i])
        # self.coef_co = derivative_coef
        return Polynomial(derivative_coef)

    # a method to find the coeffecients of the polynomial
    def get_coef(self):
        coef = []
        for i in self.coef_co:
            coef.append(i)
        return coef

    def area(self, a, b):  # area method
        self.a = a
        self.b = b
        # intilalizing the coef of the co-efficients with a zero to compensate for the constant in integration
        Integration_coef = [0]
        for i in range(len(self.coef_co)):
            # integration formula of a polynomial [x^n becomes  x^n/n+1]
            Integration_coef.append(self.coef_co[i] / (i + 1))
        p = Polynomial(Integration_coef)  # Creating a polynomial with the co-efficients
        return "Area in the interval " + str([self.a, self.b]) + " is: " + str((p[self.b] - p[self.a]))

    def Aberth(self, array):
        self.array = array
        # creating a polynomial out of the given array elemnts
        p = Polynomial([1])
        for i in self.array:
            p = p * Polynomial([-i, 1])

        coef = p.get_coef()
        degree = len(coef) - 1  # getting degree of the Polynomial
        dp = p.derivative()
        # suitable upper and lowerbounds to start Aberth's method
        upper = 1 + 1 / abs(coef[-1]) * max(abs(coef[x]) for x in range(degree))
        lower = abs(coef[0]) / (abs(coef[0]) + max(abs(coef[x]) for x in range(1, degree + 1)))
        # Starting the ABerth method by randomly choosing an estiamate for the roots
        # inside the bounds
        roots = []

        for i in range(degree):
            radius = random.uniform(lower, upper)
            angle = random.uniform(0, np.pi * 2)
            root = complex(radius * np.cos(angle), radius * np.sin(angle))
            roots.append(root)
        iteration = 0
        # calculation for Abeth's method
        while iteration < 1000:

            for i in range(len(roots)):
                ratio = p[roots[i]] / dp[roots[i]]
                offset = ratio / (1 - (ratio * sum(1 / (roots[i] - j)
                                                   for j in (roots) if j != roots[i])))

                roots[i] -= offset
            iteration += 1
        print("The estimated roots are :", roots)


q = Polynomial()
q.Aberth([0, 1, -1])