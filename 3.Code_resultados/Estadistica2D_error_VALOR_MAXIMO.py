import numpy as np

matrix = np.zeros([10, 13])

#espiral_1
M = []
M.append(1.342492)
M.append(1.450726)
M.append(1.317547)
M.append(0.975480)
M.append(1.037856)
M.append(1.720606)
M.append(1.914940)
M.append(1.992490)
M.append(2.140511)
M.append(1.931027)
M=np.array(M)
matrix[:,0] = M.transpose()
#media = np.mean(M)
#print media
print np.std(M)

#espiral_2
M1=[]
M1.append(1.641056)
M1.append(1.517190)
M1.append(1.702096)
M1.append(1.582948)
M1.append(1.789136)
M1.append(1.649797)
M1.append(1.699015)
M1.append(1.910310)
M1.append(1.893651)
M1.append(1.907301)
M1=np.array(M1)
matrix[:,1] = M1.transpose()
#media1 = np.mean(M1)
#print media1

#espiral_3
M2=[]
M2.append(1.969435)
M2.append(1.655421)
M2.append(1.892577)
M2.append(1.886906)
M2.append(1.792655)
M2.append(1.864969)
M2.append(1.878629)
M2.append(1.893393)
M2.append(1.958865)
M2.append(1.763640)
M2=np.array(M2)
matrix[:,2] = M2.transpose()

#10yaw CON AFFINE
M3=[]
M3.append(2.254643)
M3.append(1.498756)
M3.append(1.818495)
M3.append(1.838519)
M3.append(1.692168)
M3.append(1.758859)
M3.append(1.668202)
M3.append(1.943366)
M3.append(1.557716)
M3.append(1.489293)
M3=np.array(M3)
matrix[:,3] = M3.transpose()

#15yaw CON AFFINE
M4=[]
M4.append(1.754845)
M4.append(1.525344)
M4.append(1.576443)
M4.append(1.483201)
M4.append(2.148214)
M4.append(1.401104)
M4.append(2.452899)
M4.append(1.741331)
M4.append(1.649547)
M4.append(1.813738)
M4=np.array(M4)
matrix[:,4]=M4.transpose()

#20yaw CON AFFINE
M5 =[]
M5.append(2.422870)
M5.append(2.534756)
M5.append(1.626082)
M5.append(1.198512)
M5.append(1.233692)
M5.append(2.522061)
M5.append(0.949014)
M5.append(1.672218)
M5.append(1.383865)
M5.append(1.203541)
M5=np.array(M5)
matrix[:,5]=M5.transpose()    # OOOOKKKKKK

#30yaw CON AFFINE
M6=[]
M6.append(1.516675)
M6.append(1.647782)
M6.append(1.088733)
M6.append(1.844619)
M6.append(1.498481)
M6.append(2.396742)
M6.append(1.388843)
M6.append(2.969715)
M6.append(1.447969)
M6.append(1.883305)
M6=np.array(M6)
matrix[:,6]=M6.transpose()

#2cm_30yaw CON AFFINE
M7=[]
M7.append(1.970570)
M7.append(1.699833)
M7.append(1.144234)
M7.append(1.540670)
M7.append(2.395193)
M7.append(1.912584)
M7.append(1.190686)
M7.append(1.911508)
M7.append(1.664603)
M7.append(1.908026)
M7=np.array(M7)
matrix[:,7]=M7.transpose()

#10yaw SIN AFFINE
M8=[]
M8.append(2.322782)
M8.append(2.319570)
M8.append(2.248948)
M8.append(2.290096)
M8.append(2.260465)
M8.append(2.164456)
M8.append(2.197839)
M8.append(2.302598)
M8.append(2.582259)
M8.append(2.242662)
M8=np.array(M8)
matrix[:,8]=M8.transpose()

#15yaw SIN AFFINE
M9=[]
M9.append(3.906810)
M9.append(2.772137)
M9.append(2.836558)
M9.append(2.965273)
M9.append(4.147739)
M9.append(2.891096)
M9.append(4.024870)
M9.append(3.631956)
M9.append(2.786097)
M9.append(3.580675)
M9=np.array(M9)
matrix[:,9]=M9.transpose()

#20yaw SIN AFFINE
M10=[]
M10.append(4.960957)
M10.append(5.585467)
M10.append(4.381832)
M10.append(4.033405)
M10.append(4.331320)
M10.append(3.777671)
M10.append(4.056808)
M10.append(4.231361)
M10.append(4.386151)
M10.append(4.008331)
M10=np.array(M10)
matrix[:,10]=M10.transpose()

#30yaw SIN AFFINE
M11=[]
M11.append(7.641091)
M11.append(7.163972)
M11.append(8.387149)
M11.append(8.899944)
M11.append(7.348219)
M11.append(8.109229)
M11.append(8.444070)
M11.append(8.771187)
M11.append(7.722552)
M11.append(7.708225)
M11=np.array(M11)
matrix[:,11]=M11.transpose()

#2cm_30yaw SIN AFFINE
M12=[]
M12.append(19.855618)
M12.append(19.354200)
M12.append(19.120479)
M12.append(20.008811)
M12.append(19.750177)
M12.append(19.912571)
M12.append(20.098518)
M12.append(20.461918)
M12.append(20.187620)
M12.append(20.346438)
M12=np.array(M12)
matrix[:,12]=M12.transpose()
#media12 = np.mean(M12)
#print media12
print np.std(M12)

#print matrix.transpose()
print matrix.mean(axis=0)
print np.std(matrix, 0)

#matrix = np.round(matrix, decimals=4)
#print matrix

#np.savetxt('matrix.csv', matrix, delimiter=';')

















