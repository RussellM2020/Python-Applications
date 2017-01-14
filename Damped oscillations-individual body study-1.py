
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate
g=9.8
visc=0

#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


class oscillator:
    
    def __init__(self, k,b):
        
        self.state = np.array([0.0])
        self.vel = np.array([10.0])
        self.acc = np.array([0.0])
        self.k=k
        self.b=b

        self.sHistory=[]
        self.vHistory=[]
        self.aHistory=[]
        
        self.sHistory.append(self.state[0])
        self.vHistory.append(self.vel[0])
        self.aHistory.append(self.acc[0])

        self.time=0
        self.tHistory=[]
        self.tHistory.append(0)
        


    def ACC(self):

        self.acc[0]=-(self.k)*self.state[0]-(self.b)*self.vel[0]
        return self.acc

    def VEL(self):
        
        return self.vel+self.ACC()*dt
    
    def POS(self):  
        
        return self.state + ((self.vel)*dt+0.5*self.ACC()*dt**2)
        
    def step(self):
        """execute one time step of length dt and update state"""

        self.acc=self.ACC()
        self.aHistory.append(self.acc[0])
        

        self.vel=self.VEL()
        self.vHistory.append(self.vel[0])

        self.state=self.POS()
        self.sHistory.append(self.state[0])
        self.time=self.time+dt
        self.tHistory.append(self.time)
   
             
          
 
ball1=oscillator(3.0, 0.1)
dt=0.005

for i in range(10000):
    ball1.step()


fig2=plt.figure(2)
ax = plt.axes(xlim=(0,40), ylim=(-15,15))

plt.plot(ball1.tHistory, ball1.sHistory, color="r", label="Displacement")
plt.plot(ball1.tHistory, ball1.vHistory, color="b", label="Velocity")
plt.plot(ball1.tHistory, ball1.aHistory, color="g", label="Acceleration")

plt.xlabel("Time")
plt.ylabel("Motion Parameters")

 

plt.legend()
fig2.savefig("Damped Oscillations for single body-1.jpeg")






    
