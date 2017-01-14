
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate
g=9.8
visc=0

#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


#make a figure
fig = plt.figure(1)
ax = plt.axes(xlim=(-50,500), ylim=(10,500))


class falling:
    
    def __init__(self, visc):
        
        self.patch=plt.Circle((50,100),5,fc="y")
        self.visc=visc
        
        self.state = np.array([50.0,100.0])
        self.Xhistory=[]
        self.Yhistory=[]
        
        self.Xhistory.append(self.state[0])
        self.Yhistory.append(self.state[1])
        
        self.veli=np.array([10.0, 50.0])
        self.VelHistory=[]
        self.VelHistory.append(self.veli)

        self.acci=np.array([0.0, -10.0])
        self.accHistory=[]
        self.accHistory.append(self.acci)
    def position(self):  
        
        x=self.state[0]
        y=self.state[1]
        return (x,y)

    def velocity(self):

        ux=self.vel[0]
        uy=self.vel[1]
        return (ux, uy)
    
    def velocity_change(self):  
               
        new_vel = np.zeros_like(self.state)
        vlast=self.VelHistory[-1]
        acc=self.acceleration(vlast)
        new_vel[0]=vlast[0]+(acc[0]*dt)
        k= self.position()
        #collision condition
        if k[1]<20 :           
            new_vel[1]=(vlast[1]+acc[1]*dt)*-1
        else:
            new_vel[1]=vlast[1]+(acc[1]*dt)           
                   
        return new_vel
    
    def acceleration(self, vlast):
        new_acc= np.zeros_like(self.state)
        new_acc[0]=-self.visc*vlast[0]
        new_acc[1]=(-self.visc*vlast[1])-10
        self.accHistory.append(new_acc)
        return new_acc        
       

    def step(self, dt):
        """execute one time step of length dt and update state"""
        vel=self.velocity_change()
        self.VelHistory.append(vel)

        x,y=self.position()
        self.state[0]=x+vel[0]*dt
        self.state[1]=y+(vel[1]*dt-0.5*g*(dt**2))
        
        self.Xhistory.append(self.state[0])
        self.Yhistory.append(self.state[1])

          
L=[]
p=0.0015
for i in range(4):
    ball=falling(p)
    p=p*10
    L.append(ball)

dt=0.1

def init():
    for i in L:       
        ax.add_patch(i.patch)
    return i.patch,
    

def animate(i):
    for i in L:
        i.step(dt)
        i.patch.center=i.position()
    return i.patch,
   

from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)


ani = animation.FuncAnimation(fig, animate, frames=500,interval=interval,  init_func=init)

plt.show()
    
#ani.save("elasticity.mp4", writer=writer)
a=int(raw_input("enter number of trial"))

fig2=plt.figure(2)
ax = plt.axes(xlim=(-50,500), ylim=(10,500))
C=["r","b","g","y"]
d=0
for i in L:
    plt.plot(i.Xhistory, i.Yhistory, color=C[d], label=str(i.visc))
    d=d+1

plt.legend()
fig2.savefig("multiple projectile"+ str(a)+".jpeg")




    
