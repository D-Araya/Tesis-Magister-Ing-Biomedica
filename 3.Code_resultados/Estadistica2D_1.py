import numpy as np

matrix = np.zeros([10, 13])

#espiral_1
M = []
M.append(0.500)
M.append(0.581)
M.append(0.478)
M.append(0.323)
M.append(0.311)
M.append(0.504)
M.append(0.798)
M.append(0.577)
M.append(0.616)
M.append(0.591)
M=np.array(M)

matrix[:,0]=M.transpose()

#espiral_2
M1=[]
M1.append(0.421)
M1.append(0.440)
M1.append(0.409)
M1.append(0.424)
M1.append(0.412)
M1.append(0.431)
M1.append(0.454)
M1.append(0.511)
M1.append(0.486)
M1.append(0.491)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#espiral_3
M2=[]
M2.append(0.456)
M2.append(0.399)
M2.append(0.420)
M2.append(0.437)
M2.append(0.424)
M2.append(0.465)
M2.append(0.450)
M2.append(0.456)
M2.append(0.505)
M2.append(0.511)
M2=np.array(M2)
matrix[:,2]=M2.transpose()

#10yaw CON AFFINE
M3=[]
M3.append(0.415)
M3.append(0.408)
M3.append(0.559)
M3.append(0.540)
M3.append(0.547)
M3.append(0.500)
M3.append(0.561)
M3.append(0.526)
M3.append(0.506)
M3.append(0.415)   
M3=np.array(M3)
matrix[:,3]=M3.transpose()

#15yaw CON AFFINE
M4=[]
M4.append(0.627)
M4.append(0.356)
M4.append(0.377)
M4.append(0.358)
M4.append(0.853)
M4.append(0.359)
M4.append(0.462)
M4.append(0.388)
M4.append(0.459)
M4.append(0.726)
M4=np.array(M4)
matrix[:,4]=M4.transpose()

#20yaw CON AFFINE
M5 =[]
M5.append(0.806)
M5.append(0.945)
M5.append(0.381)
M5.append(0.368)
M5.append(0.305)
M5.append(0.335)
M5.append(0.262)
M5.append(0.335)
M5.append(0.329)
M5.append(0.342)
M5=np.array(M5)
matrix[:,5]=M5.transpose()    # OOOOKKKKKK

#30yaw CON AFFINE
M6=[]
M6.append(0.493)
M6.append(0.435)
M6.append(0.292)
M6.append(0.371)
M6.append(0.377)
M6.append(0.873)
M6.append(0.507)
M6.append(0.991)
M6.append(0.552)
M6.append(0.417)
M6=np.array(M6)
matrix[:,6]=M6.transpose()

#2cm_30yaw CON AFFINE
M7=[]
M7.append(0.662)
M7.append(0.696)
M7.append(0.387)
M7.append(0.461)
M7.append(0.617)
M7.append(0.634)
M7.append(0.344)
M7.append(0.573)
M7.append(0.483)
M7.append(0.519)
M7=np.array(M7)
matrix[:,7]=M7.transpose()

#10yaw SIN AFFINE
M8=[]
M8.append(0.573)
M8.append(0.565)
M8.append(0.676)
M8.append(0.671)
M8.append(0.670)
M8.append(0.652)
M8.append(0.676)
M8.append(0.667)
M8.append(0.671)
M8.append(0.581)
M8=np.array(M8)
matrix[:,8]=M8.transpose()

#15yaw SIN AFFINE
M9=[]
M9.append(0.822)
M9.append(0.727)
M9.append(0.747)
M9.append(0.730)
M9.append(0.926)
M9.append(0.723)
M9.append(0.705)
M9.append(0.728)
M9.append(0.773)
M9.append(0.963)
M9=np.array(M9)
matrix[:,9]=M9.transpose()

#20yaw SIN AFFINE
M10=[]
M10.append(1.233)
M10.append(1.249)
M10.append(1.047)
M10.append(1.038)
M10.append(0.977)
M10.append(1.113)
M10.append(0.998)
M10.append(1.050)
M10.append(1.005)
M10.append(1.049)
M10=np.array(M10)
matrix[:,10]=M10.transpose()

#30yaw SIN AFFINE
M11=[]
M11.append(1.988)
M11.append(1.952)
M11.append(1.993)
M11.append(2.006)
M11.append(1.906)
M11.append(2.040)
M11.append(1.998)
M11.append(2.088)
M11.append(2.006)
M11.append(1.985)
M11=np.array(M11)
matrix[:,11]=M11.transpose()

#2cm_30yaw SIN AFFINE
M12=[]
M12.append(5.667)
M12.append(5.631)
M12.append(5.680)
M12.append(5.836)
M12.append(5.705)
M12.append(5.786)
M12.append(5.774)
M12.append(5.895)
M12.append(5.865)
M12.append(5.862)
M12=np.array(M12)
matrix[:,12]=M12.transpose()

#print matrix

matrix = np.round(matrix, decimals=4)
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

















