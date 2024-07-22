import numpy as np
import random


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
        # self.list_co = derivative_list
        return Polynomial(derivative_list)

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

    def get_coef(self):
        coef = []
        for i in self.list_co:
            coef.append(i)
        return coef

    def Aberth(self):

        p = Polynomial(self.list_co)
        coef = p.get_coef()
        degree = len(coef) - 1
        upper = 1 + 1 / abs(coef[-1]) * max(abs(coef[x]) for x in range(degree))
        lower = abs(coef[0]) / (abs(coef[0]) + max(abs(coef[x]) for x in range(1, degree + 1)))
        roots = []
        for i in range(degree):
            radius = random.uniform(lower, upper)
            angle = random.uniform(0, np.pi * 2)
            root = complex(radius * np.cos(angle), radius * np.sin(angle))
            roots.append(root)
        # print(p)
        q = p.derivative()

        iteration = 0
        while iteration <= 10:
            for i in range(len(roots)):
                ratio = (p[roots[i]]) / (q[roots[i]])
                offset = ratio / (1 - (ratio * sum(1 / (roots[i] - j) for j in roots if j != roots[i])))
                roots[i] -= offset
            iteration += 1
        return roots


def find_root(function, a, b):
    s = function  # the continuous function
    x0, xn = a, b
    x = np.linspace(x0, xn, num=5)
    y = [s(i) for i in x]
    model = np.polyfit(x, y, len(y) - 1)  # generating a polynomial close to function
    p = Polynomial(list(model))
    roots = p.Aberth()  # finding the roots of the Polynomial via Aberth method

    # clearing out the complex roots
    index = []
    for i in range(len(roots)):
        if round(roots[i].imag, 10) == 0:
            index.append(i)
    roots1 = []
    for i in range(len(roots)):
        for j in index:
            if j == i:
                roots1.append(roots[i].real)

    roots1.sort()
    # craeting a list of numbers which are midway between the roots
    new_roots = [x0]
    for i in range(len(roots1)):
        if (i == len(roots1) - 1):
            break
        new_roots.append((roots1[i] + roots1[i + 1]) / 2)
    new_roots.append(xn)
    interval_roots = []
    # Using bisection to get the roots if it is in the sub-intervals
    for i in range(len(new_roots) - 1):
        if (s(new_roots[i]) * s(new_roots[i + 1]) < 0):
            r = round(bisection(s, new_roots[i], new_roots[i + 1]), 10)
            interval_roots.append(r)
    if len(interval_roots)==0:
        print("No roots in the interval")
    else :
        print("The roots in the interval[",a,b,"] are :\n",interval_roots)

# bisection method to find out roots
def bisection(f, a, b):
    a_n = a
    b_n = b
    N = 10000
    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
    return (a_n + b_n) / 2


find_root(lambda x: np.sin(x), -np.pi / 2, 4 * np.pi / 3)
