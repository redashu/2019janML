#!/usr/bin/python3

import  tensorflow  as  tf

#  variable  --->  constans 

#  constant  define
x=tf.constant([6])
y=tf.constant([20])

#  maths operation 

#  z=x+y  --not recommended
z=tf.add(x,y)   #  state  of  graphs 
z1=tf.multiply(x,y)

cpu_tf=tf.Session()  #  to provide cpu or  GPU 
#  can create  graphs 
mygraphdata=tf.summary.FileWriter("graph",cpu_tf.graph)
#  now you can execute  
output=cpu_tf.run(z)
output1=cpu_tf.run(z1)
print(output)
print(output1)
#  checking type of output

print(type(output))
print(type(output1))


cpu_tf.close()

