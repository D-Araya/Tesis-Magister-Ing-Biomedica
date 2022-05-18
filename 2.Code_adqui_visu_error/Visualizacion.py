# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:55:02 2015

@author: Daniel
"""
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
#import pylab as pl

data = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\datosEspiral\3-ESPIRALconZyDesplazamiento\2cm_30yaw\1_2cm_30yaw.csv', delimiter=',', unpack=True)
x1 = data[0]
y1 = data[1]
z1 = data[2]

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 2500
w.opts['azimuth'] = 270
w.opts['elevation'] = 90
w.opts['center'] = pg.Vector(0, 240, 400)
w.opts['fov'] = 24

w.setWindowTitle('Espiral de Arquimedes')
#w.setCameraPosition(distance=2500, azimuth=0, elevation = 1)

## Add a AXIS to the view
#ax = gl.GLAxisItem()
#ax.setSize(500,500,500)
#ax.translate(0, 0, 0)
#w.addItem(ax)

## Add a GRID to the view
gx = gl.GLGridItem()
gx.rotate(90, 90, 0, 0)
gx.translate(0, 0, 250)
gx.scale(40, 25, 25)
w.addItem(gx)

gz = gl.GLGridItem()
gz.setDepthValue(10)  # draw grid after surfaces since they may be translucent
gz.translate(0, 250, 0)
gz.scale(40, 25, 25)
w.addItem(gz)

##########################################################
#th = np.linspace(0, 3.5*np.pi*-1, num=1000)  # theta ->  radians
#esc = 5                          #    bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.
#a = esc*th*np.sin(th)            #    x = r cos θ, y = r sin θ    --->    x = θ cos θ, y = θ sin θ
#b = esc * th * np.cos(th) + 150  #    polar coordinates the formula of the curve is r = aθ, usually the scalar a is 1 i.e. r = θ. Polar to cartesian conversion
#c = np.zeros(1000)

##########################################################
#th = np.linspace(0, 15.5*np.pi*-1, num=1000)  # theta ->  radians
#esc = 1                          #    bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.
#a = esc*th*np.sin(th)            #    x = r cos θ, y = r sin θ    --->    x = θ cos θ, y = θ sin θ
#b = esc * th * np.cos(th) + 150  #    polar coordinates the formula of the curve is r = aθ, usually the scalar a is 1 i.e. r = θ. Polar to cartesian conversion
#c = np.zeros(1000)

####################################################3
## ESPIRAL COORD. CARTESIANAS
th = np.linspace(0, 5.5*np.pi*-1, num=1000)  # theta ->  radians
esc = 3                          #    bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.
a = esc*th*np.sin(th)            #    x = r cos θ, y = r sin θ    --->    x = θ cos θ, y = θ sin θ
b = esc * th * np.cos(th) + 150  #    polar coordinates the formula of the curve is r = aθ, usually the scalar a is 1 i.e. r = θ. Polar to cartesian conversion
c = np.zeros(1000)               #    http://stackoverflow.com/questions/22898555/how-to-write-a-spirial-function-in-python
                                 #    la  * tiene un orden de precedencia mayor que la +
## ESPIRAL COORD. POLARES
# To find the total length of a flat spiral having outer end radius = 150.798 units, inner radius = 0 units & the increase in radius per turn = 46.39 unit, the total No. of turns in the spiral is 3.25.
# 0 + 46.39938461538462 * 3.25 = 150.798
#(150.798 − 0)/3.25 = 150.798/3.25 = 46.39938461538462
# 3.25*(2*np.pi)  = 6.5*np.pi
# b = 46.39938461538462/(2*np.pi)  = 7.384691417960504    -->  http://www.intmath.com/applications-integration/12-arc-length-curve-parametric-polar.php
#  http://www.intmath.com/blog/mathematics/length-of-an-archimedean-spiral-6595
# http://www.wolframalpha.com/input/?i=%5Cint_%7B0%7D%5E%7B6.5%5Cpi%7D%5Csqrt%7B(0%2B7.384691417960504%5Ctheta)%5E2%2B(7.384691417960504)%5E2%7Dd%5Ctheta
# LONGITUD ESPIRAL -->  1555.22 mm
rho = np.sqrt(a**2 + b**2)   # arc length  -> distancia
theta = np.arctan2(b, a)  # phi  ->  radians
z = c


#pos= np.vstack([a, b, c]).transpose()
pos= np.array([a, b, c]).transpose()
#plt1 = gl.GLLinePlotItem(pos=pos, color=pg.glColor('r'), width=1.5, antialias=False)#True)
plt1 = gl.GLScatterPlotItem(pos=pos, color=pg.glColor('r'), size=2.5, pxMode=False)
w.addItem(plt1)

###################################################33
#   SEÑAL
#####################################################
#pts = np.vstack([x1, y1, z1]).transpose()
pts = data.transpose()
plt = gl.GLScatterPlotItem(pos=pts, color=pg.glColor('g'), size=2.5, pxMode=False)#True)
w.addItem(plt)
#####################################################
w.show()

##UPDATE

#def update():
 #   global plt, pts ,phase#, ptr1
  #  #pts[:-1] = pts[1:]  #elimina puntos desde el centro - shift data in the array one sample left
   # pts[1:] = pts[:-1]   #elimina puntos hacia el centro
    #plt.setData(pos=pts)
    #print 'x'


#t = pg.QtCore.QTimer()
#t.timeout.connect(update)
#t.start()


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
