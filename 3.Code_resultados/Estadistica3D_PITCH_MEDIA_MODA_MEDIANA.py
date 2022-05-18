import numpy as np

matrix = np.zeros([10, 3])

#MEDIA PITCH
M = []
M.append(25.940956)
M.append(15.364273)
M.append(23.394366)
M.append(43.610677)
M.append(30.644363)
M.append(35.790120)
M.append(42.637607)
M.append(37.956163)
M.append(28.519661)
M.append(41.089997)
M=np.array(M)
matrix[:,0]=M.transpose()
print np.mean(M)
print np.std(M)

#MODA PITCH
M1=[]
M1.append(25.305067)
M1.append(9.728769)
M1.append(21.785358)
M1.append(42.538272)
M1.append(29.704053)
M1.append(35.603269)
M1.append(43.375377)
M1.append(38.305096)
M1.append(22.310223)
M1.append(41.781691)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#MEDIANA PITCH
M2=[]
M2.append(25.305067)
M2.append(14.654424)
M2.append(22.106303)
M2.append(42.843040)
M2.append(30.538255)
M2.append(36.320101)
M2.append(42.871783)
M2.append(38.030592)
M2.append(27.888752)
M2.append(41.089997)
M2=np.array(M2)
matrix[:,2]=M2.transpose()
print np.mean(M2)
print np.std(M2)

#print matrix.transpose()
print matrix.mean(axis=0)
print np.std(matrix, 0)

#matrix = np.round(matrix, decimals=4)
#print matrix

#np.savetxt('matrix.csv', matrix, delimiter=';')

















