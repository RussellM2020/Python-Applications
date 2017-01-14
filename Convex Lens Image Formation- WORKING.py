
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate
g=9.8

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    
# Work on this slowly

#make a figure
fig = plt.figure()
ax = plt.axes(xlim=(-40,40), ylim=(-40,40))
Convex_lens=plt.Line2D((0,0), (-10,10), lw=2, color="y")#convex lens
Principal_axis=plt.Line2D((-100,100), (0,0), lw=1, color="k")#Principal axis

ax.add_line(Convex_lens)
ax.add_line(Principal_axis)
#We're going to create a class
#Each object is associated with a line, which will be refrenced by self.line
#This will help shorten and organize the code

class moving:

    def __init__(self, t1, t2,L3):

        self.line=plt.Line2D(t1,t2, lw=2.5)
        self.state = np.array([t1[0], t1[1], t2[0], t2[1]])#x1, x2, y1, y2
        self.rate=L3
        self.time_elapsed =0

    def position(self):

        return self.state
    
    def derivative_dt(self,state, t):
        dydt = np.zeros_like(state)
        
        for i in range(4):
            dydt[i]=self.rate[i]
        return dydt
    
    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.state = integrate.odeint(self.derivative_dt, self.state, [self.time_elapsed, self.time_elapsed+dt])[1]
        self.time_elapsed=self.time_elapsed+dt
        
#send in two tuples and one list. List: rate of change of [x1, x2, y1, y2]  
   


iray_p=moving((-20,0), (5,5), [0.5,0,0,0]) #this ray passes parallel to the principal axis
Object=moving((-20,-20), (0,5), [0.5,0.5,0,0])
Object.line.set_color("g")
iray2=moving((-20,400), (5,-100), [0.5,-10,0,0])#x2, y2 are scaled up because this ray goes till infinity


focal1=plt.Line2D((0,100), (5,-95), lw=2.5)#passes through (5,0)
focal2=plt.Line2D((0,-100), (5,-95), lw=2.5)

Image=plt.Line2D((20/3, 20/3), (-5/3, 0), lw=2.5, color="r")

MList=[iray_p, iray2, Object]
dt=0.1




def init():
        
        
        for i in MList:
            ax.add_line(i.line)

        ax.add_line(focal1)
        ax.add_line(focal2)
        
        ax.add_line(Image)
        
        return iray_p.line, iray2.line, Object.line, focal1, focal2, Image,
    

def animate(i):
        
        for i in MList:
            i.step(dt)
            L=i.position()
            i.line.set_data((L[0], L[1]), (L[2], L[3]))

        a,b=iray_p.line.get_data()
        flag=0
        if abs(a[0]-a[1])<=0.01:
            flag=-1
            focal1.set_visible(False)
            focal2.set_visible(False)
        elif a[0]<0:
            focal1.set_visible(True)
            focal2.set_visible(False)
            
        elif a[0]>0:
            flag=1
            focal1.set_visible(False)
            focal2.set_visible(True)

        #image position calculation
        from sympy import solve_poly_system
        from sympy.abc import x, y

        
        if flag==-1:
            Image.set_data((0,0), (5,0))
        else:
            
            ResL=[]
            imageL=[iray2, focal1, focal2]
            for i in imageL:
                if i==iray2:               
                    p,q=i.line.get_data()
                else:
                    p,q=i.get_data()
                
                
                m=(q[1]-q[0])/ (p[1]-p[0])
                
                
                e=y-q[0]-m*(x-p[0])
           
                ResL.append(e)
           
            if flag==0:

                a=solve_poly_system([ResL[0], ResL[1]], x,y) #a is a list having one tuple
                
            elif flag==1:
                a=solve_poly_system([ResL[0], ResL[2]], x,y)
        
            
            
            if a!=None:
                # there will be none case when image forms at infinity
                t1=(a[0][0], a[0][0]) #first element of the tuple
                t2=(a[0][1], 0)
                Image.set_data(t1, t2)
    
          

        return iray_p.line, iray2.line, Object.line, focal1, focal2, Image,
        

from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1500 * dt - (t1 - t0)

ani = animation.FuncAnimation(fig, animate, frames=900,interval=interval,  init_func=init)
ani.save("Convex_lens_Image_formation2.mp4", writer=writer)

plt.show()

#Grand success
#Objective 1 - Convex lens image formation- done

#the key to adjusting the length of the resulting video is "frames"
    
