import numpy as np
import math
import winsound
from time import time

#th = np.linspace(0, 3.5 * np.pi * -1, num=1000)  # theta ->  radians
#esc = 5

#th = np.linspace(0, 15.5*np.pi*-1, num=1000)  # theta ->  radians
#esc = 1

th = np.linspace(0, 5.5*np.pi*-1, num=1000) # theta ->  radians
esc = 3                          #    bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.
a = esc*th*np.sin(th)
b = esc * th * np.cos(th) + 150
c = np.zeros(1000)

pos = np.array([a, b, c]).transpose()

#ata = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\datosEspiral\3-ESPIRALconZyDesplazamiento\2cm_30yaw\10_2cm_30yaw.csv', delimiter=',', unpack=True)
data = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\\espiral_Daniel_final\1.csv', delimiter=',', unpack=True)
#data = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\datosEspiral\2-ESPIRALconZ\20yaw\2_20yaw.csv', delimiter=',', unpack=True)
#data = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\yaw30rot_circulos.csv', delimiter=',', unpack=True)
pts = data.transpose()
print pts
mat = np.vstack((data, np.ones(len(data.transpose()))))

"""
######## MATRIZ DE ROTACION - TRANSFORMACION AFFINE   -- EXPERIMENTO 2

rot = np.identity(4)
tethaY = math.radians(-30)   # ANGULO EN GRADOS --> -10, -15, -20 o -30
rot[0][0] = np.cos(tethaY)
rot[0][2] = np.sin(tethaY)
rot[2][0] = -np.sin(tethaY)
rot[2][2] = np.cos(tethaY)

PG = np.dot(rot, mat)
pts = PG[:3].transpose()
#print pts


######## TRANSFORMATION MATRIX --> TRANSLACION Y ROTACION  -- EXPERIMENTO 3

trans = np.identity(4)
trans[1][3] = -20

rot = np.identity(4)
tethaY = math.radians(-30)
rot[0][0] = np.cos(tethaY)
rot[0][2] = np.sin(tethaY)
rot[2][0] = -np.sin(tethaY)
rot[2][2] = np.cos(tethaY)

compose_matrix = np.dot(trans, rot)
PG = np.dot(compose_matrix, mat)

pts = PG[:3].transpose()
"""
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
    return winsound.Beep(Freq, Dur)
    #return np.mean(aux3), elapsed_time, winsound.Beep(Freq, Dur)

comparar(pts, pos)