import random
import matplotlib.pyplot as plt
import numpy as np
INTERVAL =2000000
pi=[]
circle_points = 0
square_points = 0

for i in range(INTERVAL):
    #print(i)
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
    origin_dist = rand_x ** 2 + rand_y ** 2
    if origin_dist <= 1:
        circle_points += 1
    square_points += 1
    pi.append(4 * circle_points / square_points)

    #print("estimate", i, "=", pi)

#print(len(pi))
#print("Final Estimation of Pi=", pi)
fig,ax=plt.subplots(1)
plt.grid(True, which='both')
p=[i for i in range(INTERVAL)]
ax.plot(p,pi,label="Monte_carlo method")
plt.axhline(y=np.pi,color='r',label="value of math.pi")
plt.ylim([3.10,3.2])
ax.legend()
plt.show()