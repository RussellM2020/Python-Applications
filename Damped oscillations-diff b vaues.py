
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
   
             
          
    
ball1=oscillator(3.0, 0.0005)
ball2=oscillator(3.0, 0.005)
ball3=oscillator(3.0, 0.05)
ball4=oscillator(3.0, 0.5)
M=[ball1, ball2, ball3, ball4]
dt=0.005

for i in range(10000):
    for j in M:
        j.step()



fig2=plt.figure(2)
ax = plt.axes(xlim=(0,50), ylim=(-10,10))
C=["r","b","g","y"]
d=0
for i in M:
    plt.plot(i.tHistory, i.sHistory, color=C[d], label="b value= "+str(i.b))
    d=d+1
plt.xlabel("Time")
plt.ylabel("Y co-ordinate")
plt.legend()
fig2.savefig("K values.jpeg")




    
