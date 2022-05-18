import numpy as np
import math
import winsound
from time import time
from scipy import stats


#th = np.linspace(0, 3.5 * np.pi * -1, num=1000)  # theta ->  radians
#esc = 5

#th = np.linspace(0, 15.5*np.pi*-1, num=1000)  # theta ->  radians
#esc = 1

th = np.linspace(0, 5.5*np.pi*-1, num=1000) # theta ->  radians
esc = 8                          #    bigger version of the same curve you've to scale (before translation) i.e. multiply both x and y values by a constant scalar.
a = esc*th*np.sin(th)
b = esc * th * np.cos(th) + 150
c = np.zeros(1000)

pos = np.array([a, b, c]).transpose()


datas = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\EstudioDeCaso\1.csv', delimiter=',', unpack=True)
#datas = np.loadtxt(r'C:\Users\Casa\PycharmProjects\Leap with Python\signal\yaw0rot_circulos.csv', delimiter=',', unpack=True)
data = datas[:3, :]  #  Tres ejes: X, Y, Z
data1 = datas[3:6, :]  # Tres angulos de orientacion: YAW, PITCH, ROLL
#data2 = datas[6:, :]

#pts = data.transpose()

mat = np.vstack((data, np.ones(len(data.transpose()))))

yaw = data1[0]
pitch = data1[1].astype(int)
#pitch1 = np.rint(data1[1]).astype(int)
roll = data1[2]
#print pitch, pitch1

media = np.mean(pitch)
moda = stats.mode(pitch)
mediana = np.median(pitch)

#PORCENTAJE DE MODA
x = len(data1[1])
y = int(moda[1])
z = (y*100)/x
print int(media)
print int(moda[0]), int(moda[1]), len(data1[1]), z, "porciento"
print int(mediana)

#media1 = np.mean(pitch1)
#moda1 = stats.mode(pitch1)
#mediana1 = np.median(pitch1)

#print int(media),  int(media1)
#print int(moda[0]),  int(moda1[0])
#print int(mediana),  int(mediana1)

######## MATRIZ DE ROTACION - TRANSFORMACION AFFINE   -- EXPERIMENTO 2
#"""
rot = np.identity(4)
tethaP = math.radians(0)
#tethaP = math.radians(int(mediana))   # ANGULO EN GRADOS --> -10, -15, -20 o -30
#tethaP = math.radians(int(moda[0]))
#tethaP = math.radians(int(mediana))
#tethaP = math.radians(int(media1))
#tethaP = math.radians(int(moda1[0]))
#tethaP = math.radians(int(mediana1))
rot[0][0] = np.cos(tethaP)
rot[0][1] = -np.sin(tethaP)
rot[1][0] = np.sin(tethaP)
rot[1][1] = np.cos(tethaP)

PG = np.dot(rot, mat)
#pts = PG[:3].transpose()
#print pts

#"""
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