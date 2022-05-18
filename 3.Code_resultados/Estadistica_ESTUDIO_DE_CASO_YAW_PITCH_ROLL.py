import numpy as np

matrix = np.zeros([10, 4])

#CON TODOS
M = []
M.append(70.166496)
M.append(88.554814)
M.append(82.474178)
M.append(81.811758)
M.append(91.914620)
M.append(118.177952)
M.append(128.783416)
M.append(130.817385)
M.append(99.262518)
M.append(85.029926)
M=np.array(M)
matrix[:,0]=M.transpose()
print np.mean(M)
print np.std(M)

#Con  Yaw-PITCH
M1=[]
M1.append(34.470863)
M1.append(21.096349)
M1.append(31.456896)
M1.append(51.962168)
M1.append(37.786223)
M1.append(47.409051)
M1.append(54.359680)
M1.append(54.086635)
M1.append(32.723413)
M1.append(51.426282)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#Con YAW-ROLL
M2=[]
M2.append(54.582643)
M2.append(75.256531)
M2.append(68.762991)
M2.append(70.656897)
M2.append(80.872934)
M2.append(99.852418)
M2.append(100.042348)
M2.append(107.584707)
M2.append(74.275091)
M2.append(69.857195)
M2=np.array(M2)
matrix[:,2]=M2.transpose()

#Con  PITCH-roll
M3=[]
M3.append(67.800145)
M3.append(85.439519)
M3.append(77.660450)
M3.append(81.037259)
M3.append(90.404911)
M3.append(114.393190)
M3.append(123.368050)
M3.append(125.523351)
M3.append(97.078475)
M3.append(83.125868)
M3=np.array(M3)
matrix[:,3]=M3.transpose()
print np.mean(M3)
print np.std(M3)


print matrix.mean(axis=0)
print np.std(matrix, 0)

#matrix = np.round(matrix, decimals=4)
#print matrix

#np.savetxt('matrix.csv', matrix, delimiter=';')

















