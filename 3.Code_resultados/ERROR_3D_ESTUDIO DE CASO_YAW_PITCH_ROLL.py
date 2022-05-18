
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import math
import winsound
from time import time

"""IMPORTANTE, EL ANGULO DE YAW SE CANCELA DEBIDO A DESEAR LOGRAR EL AJUSTE...
 VISUAL DE LA ESPIRAL SOBRE EL PATRON"""
##################### convencion ejemplo para columnas y filas:  r = mat[:, 0]   # columnas, filas

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 2500
w.opts['azimuth'] = 270
w.opts['elevation'] = 90
w.opts['center'] = pg.Vector(0, 240, 400)
w.opts['fov'] = 24

w.setWindowTitle('Espiral de Arquimedes')

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

th = np.linspace(0, 5.5 * np.pi * -1, num=1000)  # theta ->  radians
esc = 8  # bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.
a = esc * th * np.sin(th)
b = esc * th * np.cos(th) + 150
c = np.zeros(1000)

datas = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\EstudioDeCaso\10.csv', delimiter=',', unpack=True)
#datas = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\yaw0rot_circulos.csv', delimiter=',', unpack=True)
data = datas[:3, :]  #  Tres ejes: X, Y, Z
data1 = datas[3:6, :]  # Tres angulos de orientacion: YAW, PITCH, ROLL
data2 = datas[6:, :]

mat = np.vstack((data, np.ones(len(data.transpose()))))

yaw = data1[0]
pitch = data1[1]
roll = data1[2]

######## MATRIZ DE ROTACION - TRANSFORMACION AFFINE   -- ESTUDIO DE CASO YAW ########################################

rot = np.identity(4)

matriz = np.empty((mat.shape[1], 4, 4))   # X matrices de 4x4
est = np.empty(shape=[mat.shape[1], 4])
#est = np.empty((mat.shape[1], 4))
tethaY = []
for j in range(len(yaw)):
    #tethaY = math.radians(yaw[j])  # ANGULO EN GRADOS de YAW
    tethaY.append(math.radians(yaw[j]))
    #print tethaY
    rot[0][0] = np.cos(tethaY[j])
    rot[0][2] = np.sin(tethaY[j])
    rot[2][0] = -np.sin(tethaY[j])
    rot[2][2] = np.cos(tethaY[j])
    matriz[j, :, :] = np.stack(rot)
    est[j] = np.dot(matriz[j], mat.transpose()[j])   # O tambien est[j] = np.dot(rot[:], mat.transpose()[j])
#print est


######## MATRIZ DE ROTACION - TRANSFORMACION AFFINE   -- ESTUDIO DE CASO PITCH #####################################

rot1 = np.identity(4)

matriz1 = np.empty((mat.shape[1], 4, 4))   # X matrices de 4x4
est1 = np.empty(shape=[mat.shape[1], 4])
#est = np.empty((mat.shape[1], 4))
tethaP = []
for j in range(len(pitch)):
    #tethaP = math.radians(pitch[j])  # ANGULO EN GRADOS de YAW
    tethaP.append(math.radians(pitch[j]))
    #print tethaP
    rot1[0][0] = np.cos(tethaP[j])
    rot1[0][1] = -np.sin(tethaP[j])
    rot1[1][0] = np.sin(tethaP[j])
    rot1[1][1] = np.cos(tethaP[j])
    matriz1[j, :, :] = np.stack(rot1)
    est1[j] = np.dot(matriz1[j], mat.transpose()[j])   # O tambien est1[j] = np.dot(rot1[:], mat.transpose()[j])
#print est1

######## MATRIZ DE ROTACION - TRANSFORMACION AFFINE   -- ESTUDIO DE CASO ROLL #####################################

rot2 = np.identity(4)

matriz2 = np.empty((mat.shape[1], 4, 4))   # X matrices de 4x4
est2 = np.empty(shape=[mat.shape[1], 4])
#est = np.empty((mat.shape[1], 4))
tethaR = []
for j in range(len(roll)):
    #tethaR = math.radians(roll[j])  # ANGULO EN GRADOS de ROLL
    tethaR.append(math.radians(roll[j]))
    #print tethaP
    rot2[1][1] = np.cos(tethaR[j])
    rot2[1][2] = -np.sin(tethaR[j])
    rot2[2][1] = np.sin(tethaR[j])
    rot2[2][2] = np.cos(tethaR[j])
    matriz2[j, :, :] = np.stack(rot2)
    est2[j] = np.dot(matriz2[j], mat.transpose()[j])   # O tambien est2[j] = np.dot(rot2[:], mat.transpose()[j])
#print est2

pos = np.array([a, b, c]).transpose()
plt1 = gl.GLScatterPlotItem(pos=pos, color=pg.glColor('r'), size=2.5, pxMode=False)
w.addItem(plt1)

#pts = est[:, :3]  ## CON AFFINE (YAW)
#pts = est1[:, :3]  ## CON AFFINE (PITCH)
pts = est2[:, :3]  ## CON AFFINE (ROLL)
#pts = data.transpose()  ## SIN AFFINE
plt = gl.GLScatterPlotItem(pos=pts, color=pg.glColor('g'), size=2.5, pxMode=False)  # True)
w.addItem(plt)
#w.show()
########

Freq = 1000 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second

def comparar(pts, pos):
    start_time = time()
    aux = np.empty(shape=[pts.shape[0], 1])  #matriz de datos de filas igual a la cantidad de filas de los datos adquiridos (4858) y 1 columna  (4858L, 1L)
    aux2 = np.empty(shape=[pos.shape[0], 3])  #matriz de datos de filas igual a la cantidad de filas de los datos creados (espiral ideal = 1000) y 3 columna (1000L, 3L)
    for j in range(1000):   #  recorre de 1 a 1000
        aux = np.empty(shape=[pts.shape[0], 1])   # (4858L, 1L)
        for s in range(pts.shape[0]):      # recorre de 1 a 4858
            aux[s] = np.sqrt(sum(np.power(pos[j] - pts[s], 2)))  #  distancia euclidiana entre puntos       # (4884L, 1L)
        aux2[j] = pts[np.argmin(aux)]                            # (1000L, 3L)
    aux3 = np.empty(shape=[pos.shape[0], 1])   #  (1000L, 1L)
    for s in range(pos.shape[0]):  #  recorre de 1 a 1000
        aux3[s] = np.sqrt(sum(np.power(pos[s] - aux2[s], 2)))
    elapsed_time = time() - start_time
    print "Error: %f, Error Max: %f, Tiempo: %f" % (np.mean(aux3), np.max(aux3), elapsed_time)
    #print "1000 PUNTOS"
    return winsound.Beep(Freq, Dur)

comparar(pts, pos)

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


