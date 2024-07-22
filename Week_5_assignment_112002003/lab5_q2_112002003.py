from scipy import integrate
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


# least square  polynomial for a given function
def BestfitPolynomial(degree):
    co_matrix = []

    r = []
    index = 0
    dummy_degree = degree
    # similar to question 1,however instead of taking sum we integrate to get the co-effecients
    while dummy_degree <= 2 * degree: # since highest degree of the x_value could be 2*degree
        for i in range(index, dummy_degree + 1):
            s = lambda x: x ** i
            r.append(list(integrate.quad(s, 0, np.pi))[0]) # integrate with quadrature rule
        co_matrix.append(r)
        r = []
        index += 1
        dummy_degree += 1
    y_index = 0
    b = []
    while y_index <= degree:
        s = lambda x: (x ** y_index) * (np.sin(x) + np.cos(x))
        b.append(list(integrate.quad(s, 0, np.pi))[0])
        y_index += 1
    A = np.array(co_matrix) # co-effecient matrix
    B = np.array(b) # RHS of the linear equation
    sol = np.linalg.solve(A, B) # solution of the linear equation Ax=B

    a = 0
    b = np.pi

    x1 = np.linspace(a, b, num=100)
    # setting up a polynomial object to valuate a value at points and
    # using it in a plot
    p = Polynomial(sol) # creating the polynomial object
    y1 = [p[i] for i in x1]
    z1 = [np.sin(i) + np.cos(i) for i in x1]
    fig, ax = plt.subplots()

    ax.plot(x1, z1, "yo", label="$sin(x)+cos(x)$")
    ax.plot(x1, y1,"black", label="Polynomial fit for the function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Plot of Polynomial fit vs actual plot of  $sin(x)+cos(x)$",fontsize=10)
    plt.grid(True, which="both")
    print(p)
    ax.legend()
    plt.show()

# usage of the function
BestfitPolynomial(20)
