import numpy as np

matrix = np.zeros([10, 13])

#espiral_1
M = []
M.append(1.629380)
M.append(1.712523)
M.append(1.821200)
M.append(1.776323)
M.append(1.672484)
M.append(2.525692)
M.append(2.559929)
M.append(2.521774)
M.append(2.293553)
M.append(2.130988)
M=np.array(M)
matrix[:,0]=M.transpose()
print np.mean(M)
print np.std(M)

#espiral_2
M1=[]
M1.append(2.007055)
M1.append(2.043328)
M1.append(2.044179)
M1.append(1.950386)
M1.append(1.993859)
M1.append(2.082012)
M1.append(2.119944)
M1.append(2.222672)
M1.append(2.288011)
M1.append(2.151871)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#espiral_3
M2=[]
M2.append(2.279020)
M2.append(2.004239)
M2.append(2.231845)
M2.append(2.187190)
M2.append(2.114428)
M2.append(2.203558)
M2.append(2.204496)
M2.append(2.218130)
M2.append(2.305607)
M2.append(2.158036)
M2=np.array(M2)
matrix[:,2]=M2.transpose()

#10yaw CON AFFINE
M3=[]
M3.append(3.647334)
M3.append(3.723546)
M3.append(3.812440)
M3.append(3.906911)
M3.append(3.726731)
M3.append(3.770062)
M3.append(3.736935)
M3.append(3.720047)
M3.append(3.717602)
M3.append(3.652915)
M3=np.array(M3)
matrix[:,3]=M3.transpose()

#15yaw CON AFFINE
M4=[]
M4.append(3.608796)
M4.append(3.725538)
M4.append(3.833712)
M4.append(3.689588)
M4.append(3.928688)
M4.append(3.824318)
M4.append(5.078363)
M4.append(3.675277)
M4.append(3.819303)
M4.append(3.827889)
M4=np.array(M4)
matrix[:,4]=M4.transpose()

#20yaw CON AFFINE
M5 =[]
M5.append(3.764349)
M5.append(3.878768)
M5.append(4.060915)
M5.append(4.092094)
M5.append(3.811193)
M5.append(3.884388)
M5.append(3.910898)
M5.append(3.574033)
M5.append(3.465112)
M5.append(3.175355)
M5=np.array(M5)
matrix[:,5]=M5.transpose()    # OOOOKKKKKK

#30yaw CON AFFINE
M6=[]
M6.append(3.426950)
M6.append(4.142873)
M6.append(4.263819)
M6.append(4.044184)
M6.append(3.448688)
M6.append(3.313644)
M6.append(3.810615)
M6.append(3.255075)
M6.append(3.201927)
M6.append(2.902700)
M6=np.array(M6)
matrix[:,6]=M6.transpose()

#2cm_30yaw CON AFFINE
M7=[]
M7.append(4.553539)
M7.append(4.706679)
M7.append(4.222493)
M7.append(3.385419)
M7.append(4.173972)
M7.append(3.707104)
M7.append(4.653805)
M7.append(3.795582)
M7.append(3.368718)
M7.append(3.468124)
M7=np.array(M7)
matrix[:,7]=M7.transpose()

#10yaw SIN AFFINE
M8=[]
M8.append(11.016974)
M8.append(11.077425)
M8.append(11.076543)
M8.append(10.843929)
M8.append(11.070189)
M8.append(11.030581)
M8.append(11.064036)
M8.append(11.082175)
M8.append(11.370731)
M8.append(11.310478)
M8=np.array(M8)
matrix[:,8]=M8.transpose()

#15yaw SIN AFFINE
M9=[]
M9.append(15.452714)
M9.append(14.517997)
M9.append(14.556868)
M9.append(14.722262)
M9.append(14.528468)
M9.append(14.423309)
M9.append(15.021533)
M9.append(15.406264)
M9.append(14.818216)
M9.append(15.126878)
M9=np.array(M9)
matrix[:,9]=M9.transpose()

#20yaw SIN AFFINE
M10=[]
M10.append(17.280661)
M10.append(18.101600)
M10.append(17.444318)
M10.append(17.452116)
M10.append(17.764277)
M10.append(19.087202)
M10.append(19.016653)
M10.append(18.113839)
M10.append(18.017313)
M10.append(18.286878)
M10=np.array(M10)
matrix[:,10]=M10.transpose()

#30yaw SIN AFFINE
M11=[]
M11.append(28.050932)
M11.append(28.421158)
M11.append(28.111203)
M11.append(27.778199)
M11.append(28.329812)
M11.append(27.913159)
M11.append(28.314382)
M11.append(27.597878)
M11.append(27.412424)
M11.append(27.539283)
M11=np.array(M11)
matrix[:,11]=M11.transpose()

#2cm_30yaw SIN AFFINE
M12=[]
M12.append(31.262295)
M12.append(31.211707)
M12.append(30.773278)
M12.append(30.353662)
M12.append(31.089510)
M12.append(29.954667)
M12.append(30.965015)
M12.append(30.637958)
M12.append(30.755993)
M12.append(30.305446)
M12=np.array(M12)
matrix[:,12]=M12.transpose()
print np.std(M12)

#matrix = np.round(matrix, decimals=4)
#print matrix

print matrix.mean(axis=0)
print np.std(matrix, 0)

#np.savetxt('matrix.csv', matrix, delimiter=';')















