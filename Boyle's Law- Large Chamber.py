
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate
import random
g=9.8
R=2
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


#make a figure
fig = plt.figure()
ax = plt.axes(xlim=(-100,100), ylim=(-100,100))

collision_text=ax.text( -80,40,"")



class falling:
    collision=0
    
    def __init__(self, x, y,u,v): 

        self.patch=plt.Circle((x,y),R,fc="y")
        self.state = np.array([x,y])
        self.time_elapsed =0
        self.u=u
        self.v=v
        self.L=[]

    def position(self):
   
        x=self.state[0]
        y=self.state[1]
        return (x,y)

   
    def derivative_dt(self,state, t):

        print falling.collision
        vel = np.zeros_like(self.state)
        new_vel = np.zeros_like(self.state)
        
        vel[0]=self.u
        vel[1]=self.v
     
        k= self.position()
        if (k[1]<(-100+R)or k[1]>(100-R)) and (k[0]<(-100+R)or k[0]>(100-R)):
          
            new_vel[0]=(self.u)*(-1)
            new_vel[1]=(self.v)*(-1)
            
            self.L.append(new_vel)
            self.time_elapsed=0
            
            return new_vel

        elif (k[1]<(-100+R))or (k[1]>(100-R)):
            
            new_vel[0]=self.u
            new_vel[1]=(self.v)*(-1)
            
            self.L.append(new_vel)
            self.time_elapsed=0
            
            return new_vel

        elif (k[0]<(-100+R))or (k[0]>(100-R)):
        
            new_vel[0]=(self.u)*(-1)
            new_vel[1]=self.v
            
            self.L.append(new_vel)
            self.time_elapsed=0
            
            return new_vel
            
            
        return vel
    


    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.state = integrate.odeint(self.derivative_dt, self.state, [self.time_elapsed, self.time_elapsed+dt])[1]
        if self.L!=[]:
           
            self.u=self.L[0][0]
            self.v=self.L[0][1]
            falling.collision+=1
            for i in range(len(self.L)):
                w=self.L.pop()
             
        self.time_elapsed=self.time_elapsed+dt

L=[]
for i in range(7):
    p1=random.randint(-100,0)
    p2=random.randint(-100,0)
    v1=random.randint(50,70)
    v2=random.randint(50,70)
    ball=falling(p1,p2,v1,v2)
    L.append(ball)
  
dt=0.1
def init():
        
        collision_text.set_text("")
        for i in L:       
            ax.add_patch(i.patch)
       
        return i.patch, collision_text,

def animate(i):
        
        collision_text.set_text("Collisions:"+ str(falling.collision))
        
        for i in L:
            i.step(dt)
            i.patch.center=i.position()
        return i.patch, collision_text,

from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)


ani = animation.FuncAnimation(fig, animate, frames=300,interval=interval,  init_func=init)

ani.save("Large Chamber.mp4", writer=writer)
plt.show()

#Everything is working fine, only one glitch
# at high speeds, the molecules get too far behind the plot and then they execute stunted motion which is a problem. Work out a new collision strategy


    
