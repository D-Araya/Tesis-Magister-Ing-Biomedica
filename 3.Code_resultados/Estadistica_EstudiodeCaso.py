import numpy as np

matrix = np.empty([10, 2])

# ESTUDIO DE CASO CON AFFINE
M = []
M.append(98087)
M.append(0)
M.append(0)
M.append(0)
M.append(0)
M.append(0)
M.append(0)
M.append(0)
M.append(0)
M.append(0)
M=np.array(M)
matrix[:,0]=M.transpose()

# ESTUDIO DE CASO SIN AFFINE
M1=[]
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1.append(0)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#matrix = np.round(matrix, decimals=4)
print matrix

#np.savetxt('matrix.csv', matrix, delimiter=';')
