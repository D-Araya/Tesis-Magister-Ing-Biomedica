import numpy as np

matrix = np.zeros([10, 3])

#MEDIA YAW
M = []
M.append(22.733922)
M.append(14.273513)
M.append(22.293248)
M.append(42.044974)
M.append(29.758961)
M.append(36.237632)
M.append(43.946041)
M.append(41.800052)
M.append(23.852983)
M.append(39.048881)
M=np.array(M)
matrix[:,0]=M.transpose()
print np.mean(M)
print np.std(M)

#MODA YAW
M1=[]
M1.append(22.655653)
M1.append(13.116833)
M1.append(22.690506)
M1.append(42.058505)
M1.append(29.808791)
M1.append(36.124170)
M1.append(44.035304)
M1.append(41.678294)
M1.append(23.495525)
M1.append(39.028819)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#MEDIANA YAW
M2=[]
M2.append(22.655653)
M2.append(14.273513)
M2.append(22.690506)
M2.append(42.044974)
M2.append(29.808791)
M2.append(36.191037)
M2.append(44.035304)
M2.append(41.937582)
M2.append(23.603159)
M2.append(39.028819)
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

















