
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate



ka=5
kb=7

class decay:
    def __init__(self,a):
        # a is float- original number of particles of a
        self.state=np.array([a, 0.0, 0.0])
        self.ahistory=[a]        
        self.bhistory=[0.0]
        self.chistory=[0.0]
        self.time=0
        self.timeHistory=[0]
       
    def derivative_dt(self,state, t):
         rate = np.zeros_like(self.state)
                
         rate[0]=-ka*self.state[0]
         rate[1]=ka*self.state[0]-kb*self.state[1]
         rate[2]=kb*self.state[1]
         return rate

    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.state = integrate.odeint(self.derivative_dt, self.state, [self.time, self.time+dt])[1]
        self.ahistory.append(self.state[0])
        self.bhistory.append(self.state[1])
        self.chistory.append(self.state[2])
        self.time=self.time+dt
        self.timeHistory.append(self.time)
          
    
sample1=decay(50)    
dt=0.01

for i in range(100):
    sample1.step(dt)


fig2=plt.figure(2)
ax = plt.axes(xlim=(0,1), ylim=(0,50))
plt.plot(sample1.timeHistory, sample1.ahistory, color="r", label=" A particles")
plt.plot(sample1.timeHistory, sample1.bhistory, color="b", label=" B particles")
plt.plot(sample1.timeHistory, sample1.chistory, color="g", label="C particles")

plt.xlabel("Time")
plt.ylabel("Number of particles")
plt.legend()
fig2.savefig("Successive Disintegration-Tracking .jpeg")





    
