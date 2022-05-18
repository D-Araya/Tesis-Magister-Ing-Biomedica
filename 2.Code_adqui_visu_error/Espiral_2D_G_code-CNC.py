# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:41:43 2017

@author: Casa
"""

import numpy as np
import matplotlib.pyplot as plt


th = np.linspace(0, 5.5*np.pi*-1, num=1000)  # theta ->  radians
esc = 3                          #    bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.

#th = np.linspace(0, 15.5*np.pi*-1, num=1000)
#esc = 1

#th = np.linspace(0, 3.5*np.pi*-1, num=1000)
#esc = 5

a = esc*th*np.sin(th)            #    x = r cos θ, y = r sin θ    --->    x = θ cos θ, y = θ sin θ
b = esc*th*np.cos(th) + 150
print a, b

plt.plot(a, b)
plt.show()

vector = []
for i in range(0, len(a)):
    vector.append("G00 "+"X"+str(a[i])+" Y"+str(b[i]))
    # vector.append("G00 "+"X"+str(float(a[i]))+" Y"+str(float(b[i])))
    #print vector

thefile = open('test.txt', 'w')
thefile.write("%s\n" % "G21")
thefile.write("%s\n" % "G90")
for item in vector:
  print item 
  thefile.write("%s\n" % item)