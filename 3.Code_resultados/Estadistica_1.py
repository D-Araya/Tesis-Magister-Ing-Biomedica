import numpy as np

matrix = np.zeros([10, 13])

#espiral_1
M = []
M.append(0.802)
M.append(0.849)
M.append(0.787)
M.append(0.636)
M.append(0.675)
M.append(0.817)
M.append(0.992)
M.append(0.855)
M.append(0.876)
M.append(0.911)
M=np.array(M)
matrix[:,0]=M.transpose()

#espiral_2
M1=[]
M1.append(0.717)
M1.append(0.710)
M1.append(0.738)
M1.append(0.721)
M1.append(0.759)
M1.append(0.696)
M1.append(0.762)
M1.append(0.954)
M1.append(1.010)
M1.append(0.811)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#espiral_3
M2=[]
M2.append(0.724)
M2.append(0.664)
M2.append(0.657)
M2.append(0.679)
M2.append(0.676)
M2.append(0.713)
M2.append(0.687)
M2.append(0.691)
M2.append(0.736)
M2.append(0.738)
M2=np.array(M2)
matrix[:,2]=M2.transpose()

#10yaw CON AFFINE
M3=[]
M3.append(1.278)
M3.append(1.299)
M3.append(1.377)
M3.append(1.352)
M3.append(1.365)
M3.append(1.364)
M3.append(1.434)
M3.append(1.399)
M3.append(1.409)
M3.append(1.357)   
M3=np.array(M3)
matrix[:,3]=M3.transpose()

#15yaw CON AFFINE
M4=[]
M4.append(1.378)
M4.append(1.220)
M4.append(1.249)
M4.append(1.238)
M4.append(1.551)
M4.append(1.256)
M4.append(1.465)
M4.append(1.305)
M4.append(1.282)
M4.append(1.466)
M4=np.array(M4)
matrix[:,4]=M4.transpose()

#20yaw CON AFFINE
M5 =[]
M5.append(1.557)
M5.append(1.577)
M5.append(1.357)
M5.append(1.287)
M5.append(1.266)
M5.append(1.048)
M5.append(1.084)
M5.append(1.113)
M5.append(1.098)
M5.append(1.040)
M5=np.array(M5)
matrix[:,5]=M5.transpose()    # OOOOKKKKKK

#30yaw CON AFFINE
M6=[]
M6.append(1.090)
M6.append(1.115)
M6.append(1.283)
M6.append(1.123)
M6.append(1.200)
M6.append(1.309)
M6.append(1.171)
M6.append(1.351)
M6.append(1.068)
M6.append(0.960)
M6=np.array(M6)
matrix[:,6]=M6.transpose()

#2cm_30yaw CON AFFINE
M7=[]
M7.append(1.449)
M7.append(1.512)
M7.append(1.218)
M7.append(1.000)
M7.append(1.335)
M7.append(1.165)
M7.append(1.350)
M7.append(1.201)
M7.append(1.099)
M7.append(1.048)
M7=np.array(M7)
matrix[:,7]=M7.transpose()

#10yaw SIN AFFINE
M8=[]
M8.append(3.332)
M8.append(3.352)
M8.append(3.444)
M8.append(3.437)
M8.append(3.423)
M8.append(3.382)
M8.append(3.407)
M8.append(3.409)
M8.append(3.380)
M8.append(3.359)
M8=np.array(M8)
matrix[:,8]=M8.transpose()

#15yaw SIN AFFINE
M9=[]
M9.append(4.705)
M9.append(4.590)
M9.append(4.593)
M9.append(4.600)
M9.append(4.727)
M9.append(4.611)
M9.append(4.525)
M9.append(4.666)
M9.append(4.651)
M9.append(4.741)
M9=np.array(M9)
matrix[:,9]=M9.transpose()

#20yaw SIN AFFINE
M10=[]
M10.append(6.079)
M10.append(6.094)
M10.append(6.019)
M10.append(5.933)
M10.append(5.969)
M10.append(5.943)
M10.append(5.916)
M10.append(5.999)
M10.append(5.964)
M10.append(5.908)
M10=np.array(M10)
matrix[:,10]=M10.transpose()

#30yaw SIN AFFINE
M11=[]
M11.append(8.397)
M11.append(8.359)
M11.append(8.386)
M11.append(8.392)
M11.append(8.412)
M11.append(8.397)
M11.append(8.375)
M11.append(8.433)
M11.append(8.360)
M11.append(8.311)
M11=np.array(M11)
matrix[:,11]=M11.transpose()

#2cm_30yaw SIN AFFINE
M12=[]
M12.append(10.642)
M12.append(10.617)
M12.append(10.675)
M12.append(10.790)
M12.append(10.653)
M12.append(10.749)
M12.append(10.720)
M12.append(10.849)
M12.append(10.811)
M12.append(10.844)
M12=np.array(M12)
matrix[:,12]=M12.transpose()

#print matrix

#matrix = np.round(matrix, decimals=4)
#print matrix

MEDIAMASDESVIACION = np.zeros([2, 13])
E=[]
E.append(np.mean(M))
E.append(np.std(M))
E=np.array(E)
MEDIAMASDESVIACION[:,0]=E.transpose()

E1=[]
E1.append(np.mean(M1))
E1.append(np.std(M1))
E1=np.array(E1)
MEDIAMASDESVIACION[:,1]=E1.transpose()

E2=[]
E2.append(np.mean(M2))
E2.append(np.std(M2))
E2=np.array(E2)
MEDIAMASDESVIACION[:,2]=E2.transpose()

E3=[]
E3.append(np.mean(M3))
E3.append(np.std(M3))
E3=np.array(E3)
MEDIAMASDESVIACION[:,3]=E3.transpose()

E4=[]
E4.append(np.mean(M4))
E4.append(np.std(M4))
E4=np.array(E4)
MEDIAMASDESVIACION[:,4]=E4.transpose()

E5=[]
E5.append(np.mean(M5))
E5.append(np.std(M5))
E5=np.array(E5)
MEDIAMASDESVIACION[:,5]=E5.transpose()

E6=[]
E6.append(np.mean(M6))
E6.append(np.std(M6))
E6=np.array(E6)
MEDIAMASDESVIACION[:,6]=E6.transpose()

E7=[]
E7.append(np.mean(M7))
E7.append(np.std(M7))
E7=np.array(E7)
MEDIAMASDESVIACION[:,7]=E7.transpose()

E8=[]
E8.append(np.mean(M8))
E8.append(np.std(M8))
E8=np.array(E8)
MEDIAMASDESVIACION[:,8]=E8.transpose()

E9=[]
E9.append(np.mean(M9))
E9.append(np.std(M9))
E9=np.array(E9)
MEDIAMASDESVIACION[:,9]=E9.transpose()

E10=[]
E10.append(np.mean(M10))
E10.append(np.std(M10))
E10=np.array(E10)
MEDIAMASDESVIACION[:,10]=E10.transpose()

E11=[]
E11.append(np.mean(M11))
E11.append(np.std(M11))
E11=np.array(E11)
MEDIAMASDESVIACION[:,11]=E11.transpose()

E12=[]
E12.append(np.mean(M12))
E12.append(np.std(M12))
E12=np.array(E12)
MEDIAMASDESVIACION[:,12]=E12.transpose()

MSD = np.array(MEDIAMASDESVIACION)
print MSD

#np.savetxt('matrix.csv', matrix, delimiter=';')

















