import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8
L = 2 # length of the pendulum
t = 100 # time
# initial condition
theta_0 = np.pi/3
d_theta_0 = 0

# getting d^2(theta)/d(theta)^2
def get_d2_theta(theta):
    return  -(g/L)*np.sin(theta)

# using Euler's method to solve the system
def theta(t):
    theta = theta_0
    d_theta = d_theta_0
    delta_t = 1./60 # increment
    for time in np.arange(0,t,delta_t):
        d2_theta = get_d2_theta(theta)
        theta =theta + d_theta*delta_t
        d_theta =d_theta+ d2_theta*delta_t
    return theta
# plot for the pendulum
x_data = [0,0]
y_data = [0,0]

fig, ax = plt.subplots()
ax.set_title("Animation emulating the motion of a pendulum",fontsize=10)
ax.plot([-0.5,0.5],[0,0],"black",linewidth=3) # upper part of the pendulum
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5,1)
line, = ax.plot(0, 0)

def animation_frame(i):
    x = L*np.sin(theta(i)) # L *sin(theta)
    y = -L*np.cos(theta(i)) # -L *cos(theta)

    x_data[1] = x
    y_data[1] = y

    line.set_xdata(x_data)
    line.set_ydata(y_data)

    return line,
# Animation for the pendulum
animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 60, (1./60)),interval = 10)

plt.show()
