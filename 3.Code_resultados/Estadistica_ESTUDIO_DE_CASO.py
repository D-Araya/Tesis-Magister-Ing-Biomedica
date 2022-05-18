import numpy as np

matrix = np.zeros([10, 4])

#Sin trans. afIn
M = []
M.append(22.390427)
M.append(9.728769)
M.append(21.785358)
M.append(42.030972)
M.append(29.704053)
M.append(35.938678)
M.append(43.263131)
M.append(41.179947)
M.append(22.854677)
M.append(38.972699)
M=np.array(M)
matrix[:,0]=M.transpose()
print np.mean(M)
print np.std(M)

#Con  Yaw
M1=[]
M1.append(27.687333)
M1.append(16.545976)
M1.append(27.931204)
M1.append(48.017140)
M1.append(34.530857)
M1.append(40.957614)
M1.append(48.345649)
M1.append(45.966293)
M1.append(27.156655)
M1.append(44.132392)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#Con Pitch
M2=[]
M2.append(27.106092)
M2.append(13.836098)
M2.append(24.914107)
M2.append(44.417329)
M2.append(30.789711)
M2.append(36.895030)
M2.append(43.673382)
M2.append(39.688050)
M2.append(25.851393)
M2.append(41.526020)
M2=np.array(M2)
matrix[:,2]=M2.transpose()

#Con  roll
M3=[]
M3.append(53.272143)
M3.append(74.119447)
M3.append(67.006418)
M3.append(70.716610)
M3.append(80.076648)
M3.append(97.374390)
M3.append(101.183116)
M3.append(106.142889)
M3.append(76.399879)
M3.append(68.934406)
M3=np.array(M3)
matrix[:,3]=M3.transpose()
print np.mean(M3)
print np.std(M3)

print matrix.mean(axis=0)
print np.std(matrix, 0)

#matrix = np.round(matrix, decimals=4)
#print matrix

#np.savetxt('matrix.csv', matrix, delimiter=';')

















