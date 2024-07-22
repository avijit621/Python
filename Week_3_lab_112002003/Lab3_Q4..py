import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
class Polynomial:
    def __init__(self,list_co=[]):
        self.list_co=list_co

    def __str__(self):
        strings=[]
        strings.append("Coefficients of the polynomial are:")
        temp =  " ".join([str(x) for x in self.list_co])
        strings.append(str(temp))
        return "\n".join(strings)
    #Evaluating the polynomial at a point and using getitem to hget the value
    def __getitem__(self, item):
        return sum([(item ** i) * self.list_co[i] for i in range(len(self.list_co))])
    # Defining addition of Polynom,ials properly
    def __add__(self, other):
            size=max(len(self.list_co),len(other.list_co))
            sum=[0 for i in range(size)]
            for i in range(0,len(self.list_co),1):
                 sum[i]=self.list_co[i]
            for i in range(len(other.list_co)):
                sum[i]+=other.list_co[i]
            self.list_co=sum    
            return self
    # defining Subtraction properly
    def __sub__(self, other):
            size=max(len(self.list_co),len(other.list_co))
            sum=[0 for i in range(size)]
            for i in range(0,len(self.list_co),1):
                 sum[i]=self.list_co[i]
            for i in range(len(other.list_co)):
                sum[i]-=other.list_co[i]
            self.list_co=sum    
            return self
    # Defining constant multiplication
    def __rmul__(self, other):
        vector = self.list_co
        for i in range(len(vector)):
            self.list_co[i] = other * self.list_co[i]
        return self
    # defining multiplication of two ploynomials
    def __mul__(self, other):
        r1=len(self.list_co)
        r2=len(other.list_co)
        prod=[0]*(r1+r2-1)
        for i in range(r1):
            for j in range(r2):
                prod[i+j]+=self.list_co[i]*other.list_co[j]
        self.list_co=prod
        return self
    # plot the polynomial in an interval
    def show(self,a,b):
        self.a=a
        self.b=b
        r=(self.b-self.a)/5
        x=np.arange(self.a,self.b+r,r)
        # setting up a polynomial object to valuate a value at points and
        # using it in a plot
        p=Polynomial(self.list_co)
        y=[p[i]for i in x]
        fig,ax=plt.subplots()
        ax.plot(x,y)
        s=[p[self.a],p[self.b]]
        s.sort()
        ax.set_ylim(s)
        ax.set_xlabel("x")
        ax.set_ylabel("p(x)")

        ax.set_title("Plot of the Polynomial")
        ax.set_xlim(self.a,self.b)
        plt.grid(True,which="both")
        plt.show()

    def fitViaMatrixMethod(self,plot_val):
        self.plot_val=plot_val
        x_val=[]
        y_val=[]
        s=[]
        # setting X values and y values separately
        for i in range (len(self.plot_val)):
            x_val.append(self.plot_val[i][0])
            y_val.append(self.plot_val[i][1])
        # evaluating the co-efecient matrix
        for i in range(len(self.plot_val)):
             s.append([x_val[i]**j for j in range(len(self.plot_val))])
        A=np.array(s)
        b=np.array(y_val)
        # using linalg module to solve the linear equation
        x=np.linalg.solve(A,b)
        p=Polynomial(x)
        fig,ax=plt.subplots()
        r=(max(x_val)-min(x_val))/5
        x=np.arange(min(x_val),max(x_val)+0.5,0.5)
        ax.plot(x_val,y_val,"ro")
        y=[p[i] for  i in x]
        ax.set_ylabel("p(x)")
        ax.set_xlabel("x")
        ax.set_title("Polynomial interpolation using matrix method")
        plt.grid(True, which="both")
        # in order to make the plot smooth
        xnew = np.linspace(x.min(), x.max(), 300)

        spl = make_interp_spline(x, y, k=3)  # type: BSpline
        y_smooth = spl(xnew)

        plt.plot(xnew, y_smooth)
        plt.show()

    def fitViaLagrangePoly(self,plo_val):
        self.plot_val=plo_val
        x_val = []
        y_val = []
        #A plynomial to store the numerartor of the lagrange method
        s = {i : Polynomial([1]) for i in range(len(self.plot_val)) }
        a=Polynomial([1])
        # list to store the denominator of the lagrange method
        denom=[]
        b=1
        for i in range(len(self.plot_val)):
            x_val.append(self.plot_val[i][0])
            y_val.append(self.plot_val[i][1])
        # creating the denominator and numerator for each x value
        for i in  range(len(self.plot_val)):
            for j in range(len(x_val)):
                if j!=i:
                    p=Polynomial([-x_val[j],1])
                    # getting the polynomial multiplication in numerator
                    b=b*(x_val[i]-x_val[j])
                    a=a*p
            s[i]=s[i]*a # storing the polynomials in a dictionary
            denom.append(b)
            a=Polynomial([1])
            b=1

        l=Polynomial([0]) # to hold the numerator of the lagrange method
        for i in range(len(y_val)):
            l=l+y_val[i]*((1/denom[i])*s[i]) # Estimating the polynomial
        #Setting up the plot
        x=np.arange(min(x_val),max(x_val)+0.5,0.5)
        fig,ax=plt.subplots()
        ax.plot(x_val,y_val,"ro")
        y=[l[i] for  i in x]
        ax.set_ylabel("p(x)")
        ax.set_xlabel("x")
        ax.set_title("Polynomial interpolation using matrix method")
        plt.grid(True, which="both")
        xnew = np.linspace(x.min(), x.max(), 300)

        spl = make_interp_spline(x, y, k=3)  # type: BSpline
        y_smooth = spl(xnew)

        plt.plot(xnew, y_smooth)
        plt.show()    
        


        










#p1=Polynomial([-1,1])
#p2=Polynomial([1,1,1])
#p=p1*p2
#print(p)
#p=Polynomial([1,0,1])
#p.show(1,2)
#p=Polynomial([1,2,3,4])
p=Polynomial([])
p.fitViaMatrixMethod([(0,1), (1,4), (-1, 0), (2, 15),(3,12)])
p.fitViaLagrangePoly([(0,1), (1,4), (-1, 0), (2, 15),(3,12)])
#p1=Polynomial([1,2,3])
#p2=p1-p1
#print(p2)