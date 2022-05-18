import numpy as np

matrix = np.zeros([10, 13])

#espiral_1
M = []
M.append(0.80289329489283101)
M.append(0.84978094713068963)
M.append(0.78781085009508278)
M.append(0.63609609572159687)
M.append(0.67599325486663664)
M.append(0.81710439233219789)
M.append(0.99256675950295725)
M.append(0.85554896140326953)
M.append(0.8766133588165651)
M.append(0.91127520847217047)
M=np.array(M)
matrix[:,0]=M.transpose()

#espiral_2
M1=[]
M1.append(0.71754030029745652)
M1.append(0.71055945932598674)
M1.append(0.73871475402254283)
M1.append(0.72111342831781533)
M1.append(0.75952415544263474)
M1.append(0.69640965792798459)
M1.append(0.76219865914498086)
M1.append(0.95486643575005492)
M1.append(1.0104481451649023)
M1.append(0.81197898044541561)
M1=np.array(M1)
matrix[:,1]=M1.transpose()

#espiral_3
M2=[]
M2.append(0.72443010625465276)
M2.append(0.66457841489924474)
M2.append(0.6572182464753904)
M2.append(0.67996750444824394)
M2.append(0.67678755509028155)
M2.append(0.71395209045728969)
M2.append(0.68714267059225287)
M2.append(0.69135378555393823)
M2.append(0.73616053538349158)
M2.append(0.73854994656919737)
M2=np.array(M2)
matrix[:,2]=M2.transpose()

#10yaw CON AFFINE
M3=[]
M3.append(1.2787987617064189)
M3.append(1.2997690343334221)
M3.append(1.3773450848822775)
M3.append(1.3522232055729781)
M3.append(1.3659686846161916)
M3.append(1.364045871456228)
M3.append(1.4343813434560597)
M3.append(1.399019479714767)
M3.append(1.4095044634741289)
M3.append(1.3575917601390712)   
M3=np.array(M3)
matrix[:,3]=M3.transpose()

#15yaw CON AFFINE
M4=[]
M4.append(1.37802538397953)
M4.append(1.2200956025688188)
M4.append(1.249997484883304)
M4.append(1.2381337711469149)
M4.append(1.5518130514536073)
M4.append(1.2566881464504787)
M4.append(1.4659074624436341)
M4.append(1.3055358981501)
M4.append(1.2826915378191097)
M4.append(1.4661501619919453)
M4=np.array(M4)
matrix[:,4]=M4.transpose()

#20yaw CON AFFINE
M5 =[]
M5.append(1.5574728158289208)
M5.append(1.5772878441570919)
M5.append(1.3578578816487092)
M5.append(1.2872747233397588)
M5.append(1.2667146833866592)
M5.append(1.0487303779370636)
M5.append(1.0845289515651524)
M5.append(1.1134583948459409)
M5.append(1.0980053969047354)
M5.append(1.0401007302074823)
M5=np.array(M5)
matrix[:,5]=M5.transpose()    # OOOOKKKKKK

#30yaw CON AFFINE
M6=[]
M6.append(1.0900413283641517)
M6.append(1.115568176285693)
M6.append(1.2836617362872247)
M6.append(1.1232768011132126)
M6.append(1.2002745117241203)
M6.append(1.3096590908777062)
M6.append(1.1717195457700336)
M6.append(1.3515165191724547)
M6.append(1.0685114288556228)
M6.append(0.96056576852874243)
M6=np.array(M6)
matrix[:,6]=M6.transpose()

#2cm_30yaw CON AFFINE
M7=[]
M7.append(1.4490701471652014)
M7.append(1.5122033683418021)
M7.append(1.2180703950194618)
M7.append(1.0004502855843551)
M7.append(1.3356143898970974)
M7.append(1.165650287823693)
M7.append(1.350340298777434)
M7.append(1.2010011893647494)
M7.append(1.099504607141143)
M7.append(1.0489776724401449)
M7=np.array(M7)
matrix[:,7]=M7.transpose()

#10yaw SIN AFFINE
M8=[]
M8.append(3.3325358245337138)
M8.append(3.352428049326647)
M8.append(3.4443329473676267)
M8.append(3.4370500138209921)
M8.append(3.4239289901780285)
M8.append(3.3825704076661376)
M8.append(3.4073095728251421)
M8.append(3.4093094027233808)
M8.append(3.3806446889774602)
M8.append(3.3591487268209659)
M8=np.array(M8)
matrix[:,8]=M8.transpose()

#15yaw SIN AFFINE
M9=[]
M9.append(4.7050619981874746)
M9.append(4.5904513978266257)
M9.append(4.5939618405865312)
M9.append(4.600862254789674)
M9.append(4.7275503929794027)
M9.append(4.6112303157365702)
M9.append(4.5256838967674193)
M9.append(4.6669721517115308)
M9.append(4.6514247830892268)
M9.append(4.7417865050506407)
M9=np.array(M9)
matrix[:,9]=M9.transpose()

#20yaw SIN AFFINE
M10=[]
M10.append(6.0790778939826797)
M10.append(6.0944932043012017)
M10.append(6.0198969037349537)
M10.append(5.9336714646341679)
M10.append(5.9691913709672093)
M10.append(5.9439402358728692)
M10.append(5.9164203898418899)
M10.append(5.99908083198798)
M10.append(5.9647163492236688)
M10.append(5.9085509547734949)
M10=np.array(M10)
matrix[:,10]=M10.transpose()

#30yaw SIN AFFINE
M11=[]
M11.append(8.3970307413203891)
M11.append(8.3596299555901421)
M11.append(8.3868949542995477)
M11.append(8.3926445200289699)
M11.append(8.4121909225203719)
M11.append(8.397606565641901)
M11.append(8.3758288835925185)
M11.append(8.4338643716651305)
M11.append(8.3601495023173342)
M11.append(8.311847733497352)
M11=np.array(M11)
matrix[:,11]=M11.transpose()

#2cm_30yaw SIN AFFINE
M12=[]
M12.append(10.642072059901578)
M12.append(10.617879524094393)
M12.append(10.675514621542833)
M12.append(10.790662142056824)
M12.append(10.653280905720845)
M12.append(10.749075501541412)
M12.append(10.720046991134508)
M12.append(10.849491279919315)
M12.append(10.811168180881758)
M12.append(10.844884854166912)
M12=np.array(M12)
matrix[:,12]=M12.transpose()

print matrix

matrix = np.round(matrix, decimals=4)
print matrix

#np.savetxt('matrix.csv', matrix, delimiter=';')
















