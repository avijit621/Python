import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
def estimatePi(INTERVAL):
          
          pi=[]
          circle_points = 0
          square_points = 0
          
          for i in range(INTERVAL):
              
              rand_x = random.uniform(-1, 1) # uniformly choosing the x-cordinate
              
              rand_y = random.uniform(-1, 1) # uniformly choosing the y-coordinate
              
              # checking whether it lies inside the circle or the square 
              origin_dist = rand_x ** 2 + rand_y ** 2
              if origin_dist <= 1:
                  circle_points += 1
              square_points += 1
              pi.append(4 * circle_points / square_points)
          
          fig,ax=plt.subplots(1)
          plt.grid(True, which='both')
          p=[i for i in range(INTERVAL)]
          #p=p *1e4
          ax.plot(p,pi,label="Monte_carlo method")
          plt.axhline(y=np.pi,color='r',label="value of math.pi")
          plt.ylim([3.10,3.2])
          ax.legend()
          ax.set_title("Estimating "+ str(r'$\pi$')+ " using Monte-Carlo method" )
          ax.set_xlabel("No of points generated")
          ax.set_ylabel("4 x fraction of points within the circle")
          for tick in ax.get_xticklabels():
              tick.set_rotation(45)
          f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
          g = lambda x, pos: "${}$".format(f._formatSciNotation('%0.5e' % x))
          plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))

          plt.show()
estimatePi(2000000)          