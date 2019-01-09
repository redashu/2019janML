#!/usr/bin/env python3
import matplotlib.pyplot   as  plt
import  mpld3
x=[4,7,9,12]
y=[6,9,6,10]

players=["virat","dhoni","pa"]
runs=[400,450,66]

plt.xlabel('Time')
plt.ylabel('Distance')
plt.grid(c='red')
plt.plot(x,y,label="danger")  #  to plot graph in maths way
plt.plot(y,x,label="smooth")
plt.bar(x,y) #  to plot graph in bar format 
#plt.bar(players,runs) #  to plot graph in bar format 
#plt.bar(y,x)
plt.scatter(x,y,s=200,marker='x',label="mines")
plt.scatter(y,x,s=150,marker='*',label="rocks")
plt.legend()
plt.show()
#mpld3.show()

