
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate
g=9.8

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


#make a figure
fig = plt.figure()
ax = plt.axes(xlim=(30,500), ylim=(-50,100))
patch=plt.Circle((50,100),5,fc="y")



class falling:
    
    def __init__(self):
        
        self.state = np.array([50.0,100.0])
        self.time_elapsed =0
        self.u=np.zeros_like(self.state)
        self.L=[]
        self.a=[4.5, 2.5]
        self.flag=1

    def position(self):      
                
        x=self.state[0]
        y=self.state[1]
        return (x,y)

   
    def derivative_dt(self,state, t):
        
        vel = np.zeros_like(self.state)
        new_vel = np.zeros_like(self.state)

        #leftincline velocity
        if self.flag==1:
            vel[0]=self.u[0]+ self.a[0]*t
            vel[1]= self.u[1]-self.a[1]*t


        #rightincline velocity
        elif self.flag==-1:

            vel[0]=self.u[0]- self.a[0]*t
            vel[1]= self.u[1]-self.a[1]*t         
               
        k= self.position()
        #leftincline collision
        if k[1]<20 and self.flag==1:
            new_vel[0]=(self.u[0]+ self.a[0]*t)
            new_vel[1]= (self.u[1]-self.a[1]*t)*-1                      
            
            self.L.append(new_vel)            
            self.time_elapsed=0            
            return new_vel

        #rightincline collision
        elif k[1]<20 and self.flag==-1:
            new_vel[0]=(self.u[0]- self.a[0]*t)
            new_vel[1]= (self.u[1]-self.a[1]*t)*-1                     
            
            self.L.append(new_vel)            
            self.time_elapsed=0            
            return new_vel
        return vel

    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.state = integrate.odeint(self.derivative_dt, self.state, [self.time_elapsed, self.time_elapsed+dt])[1]
        if self.L!=[]:
            self.u=self.L.pop()
            self.flag=self.flag*-1
        self.time_elapsed=self.time_elapsed+dt
        
  
    
ball=falling()    
dt=0.1

def init():
        patch.center = (50,100)
          
        ax.add_patch(patch)
        return patch,

def animate(i):
        
        ball.step(dt)
        patch.center=ball.position()
        return patch,

from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)


ani = animation.FuncAnimation(fig, animate, frames=300,interval=interval,  init_func=init)

ani.save("Gallileo.mp4", writer=writer)
plt.show()



    
