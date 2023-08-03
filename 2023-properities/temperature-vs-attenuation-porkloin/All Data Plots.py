import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Fund1 = pd.read_csv('Fund_1.csv')
data1 = np.array(Fund1)
T1 = data1[0:18,0]
A1 = data1[0:18,1]
#-----------------------------------
Fund2 = pd.read_csv('Fund_2.csv')
data2 = np.array(Fund2)
T2 = data2[0:21,0]
A2 = data2[0:21,1]
#-----------------------------------
Fund3 = pd.read_csv('Fund_3.csv')
data3 = np.array(Fund3)
T3 = data3[:,0]
A3 = data3[:,1]
#-----------------------------------
ThirdHarm1 = pd.read_csv('3rdHarm_1.csv')
data4 = np.array(ThirdHarm1)
T4 = data4[:,0]
A4 = data4[:,1]
#----------------------------------
ThirdHarm2 = pd.read_csv('3rdHarm_2.csv')
data5 = np.array(ThirdHarm2)
T5 = data5[:,0]
A5 = data5[:,1]
#----------------------------------
ThirdHarm3 = pd.read_csv('3rdHarm_3.csv')
data6 = np.array(ThirdHarm3)
T6 = data6[:,0]
A6 = data6[:,1]
#----------------------------------


t20 = []
t21 = []
t25 = []
t26 = []
t30 = []
t35 = []
t40 = []
t45 = []
t50 = []
t55 = []
t60 = []

T20 = []
T21 = []
T25 = []
T26 = []
T30 = []
T35 = []
T40 = []
T45 = []
T50 = []

A20 = []
A21 = []
A25 = []
A26 = []
A30 = []
A35 = []
A40 = []
A45 = []
A50 = []






a20 = []
a21 = []
a25 = []
a26 = []
a30 = []
a35 = []
a40 = []
a45 = []
a50 = []
a55 = []
a60 = []

for i in range(0,3):
    t20.append(T1[i])
    a20.append(A1[i])
    t26.append(T1[i+3])
    a26.append(A1[i+3])
    t30.append(T1[i+6])
    a30.append(A1[i+6])
    t40.append(T1[i+9])
    a40.append(A1[i+12])
    t45.append(T1[i+12])
    a45.append(A1[i+12])
    t50.append(T1[i+15])
    a50.append(A1[i+15])
    
    t21.append(T2[i])
    a21.append(A2[i])
    t25.append(T2[i+3])
    a25.append(A2[i+3])
    if i<2:
        t30.append(T2[i+6])
        a30.append(A2[i+6])
    t35.append(T2[i+8])
    a35.append(A2[i+8])
    t40.append(T2[i+11])
    a40.append(A2[i+11])
    t45.append(T2[i+14])
    a45.append(A2[i+14])
    t50.append(T2[i+17])
    a50.append(A2[i+17])

    t21.append(T3[i])
    a21.append(A3[i])
    t25.append(T3[i+3])
    a25.append(A3[i+3])
    t30.append(T3[i+6])
    a30.append(A3[i+6])
    t35.append(T3[i+9])
    a35.append(A3[i+9])
    t40.append(T3[i+13])
    a40.append(A3[i+13])
    t45.append(T3[i+16])
    a45.append(A3[i+16])
    t50.append(T3[i+19])
    a50.append(A3[i+19])
    t55.append(T3[i+22])
    a55.append(A3[i+22])
    t60.append(T3[i+25])
    a60.append(A3[i+25])

    T20.append(T4[i])
    A20.append(A4[i])
    T25.append(T4[i+3])
    A25.append(A4[i+3])
    T30.append(T4[i+6])
    A30.append(A4[i+6])
    if i<2:
        T35.append(T4[i+9])
        A35.append(A4[i+9])
    T40.append(T4[i+11])
    A40.append(A4[i+11])
    T45.append(T4[i+14])
    A45.append(A4[i+14])
    T50.append(T4[i+17])
    A50.append(A4[i+17])

    T21.append(T5[i])
    A21.append(A5[i])
    T25.append(T5[i+3])
    A25.append(A5[i+3])
    T30.append(T5[i+6])
    A30.append(A5[i+6])
    T35.append(T5[i+9])
    A35.append(A5[i+9])
    T40.append(T5[i+12])
    A40.append(A5[i+12])
    T45.append(T5[i+15])
    A45.append(A5[i+15])
    T50.append(T5[i+18])
    A50.append(A5[i+18])

    T21.append(T6[i])
    A21.append(A6[i])
    T25.append(T6[i+3])
    A25.append(A6[i+3])
    T30.append(T6[i+6])
    A30.append(A6[i+6])
    T35.append(T6[i+9])
    A35.append(A6[i+9])
    T40.append(T6[i+12])
    A40.append(A6[i+12])
    T45.append(T6[i+15])
    A45.append(A6[i+15])
    T50.append(T6[i+18])
    A50.append(A6[i+18])

    

t30.append(T3[12])
a30.append(A3[12])

t50.append(T2[20])
a50.append(A2[20])

T50.append(T4[20])
A50.append(A4[20])




    





avg20 = sum(a20)/len(a20)
avg21 = sum(a21)/len(a21)
avg25 = sum(a25)/len(a25)
avg26 = sum(a26)/len(a26)
avg30 = sum(a30)/len(a30)
avg35 = sum(a35)/len(a35)
avg40 = sum(a40)/len(a40)
avg45 = sum(a45)/len(a45)
avg50 = sum(a50)/len(a50)
avg55 = sum(a55)/len(a55)
avg60 = sum(a60)/len(a60)

Avg20 = sum(A20)/len(A20)
Avg21 = sum(A21)/len(A21)
Avg25 = sum(A25)/len(A25)
Avg30 = sum(A30)/len(A30)
Avg35 = sum(A35)/len(A35)
Avg40 = sum(A40)/len(A40)
Avg45 = sum(A45)/len(A45)
Avg50 = sum(A50)/len(A50)

avg = [avg20,avg21,avg25,avg26,avg30,avg35,avg40,avg45,avg50,avg55,avg60]
Avg = [Avg20,Avg21,Avg25,Avg30,Avg35,Avg40,Avg45,Avg50]
ts = [20,21,25,26,30,35,40,45,50,55,60]
Ts = [20,21,25,30,35,40,45,50]



plt.figure()
plt.scatter(ts,avg,marker='x',color='b')
plt.scatter(Ts,Avg,marker='x',color='r')
plt.plot(ts,avg,color='b',label='476 kHz')
plt.plot(Ts,Avg,color='r',label='1.5975 MHz')
plt.xlabel('Temperature [°C]')
plt.ylabel('Attenuation coefficient [np/cm]')
plt.legend()
plt.grid(True)
#plt.show()



#Fundamental frequency plots
plt.figure()
plt.scatter(T1,A1,label = 'May 16')
plt.scatter(T2,A2,label = 'May 18')
plt.scatter(T3,A3,label = 'May 24')
plt.xlabel('Temperature [°C]')
plt.ylabel('Attenuation coefficient [np/cm]')
plt.legend()
plt.grid(True)
#plt.show()

#Third harmonic plots
plt.figure()
plt.scatter(T4,A4,label = 'July 5')
plt.scatter(T5,A5,label = 'July 14')
plt.scatter(T6,A6,label = 'July 19')
plt.xlabel('Temperature [°C]')
plt.ylabel('Attenuation coefficient [np/cm]')
plt.legend()
plt.grid(True)
#plt.show()

#All plots
plt.figure()
plt.scatter(T1,A1,label = 'May 16 (476 kHz)')
plt.scatter(T2,A2,label = 'May 18 (476 kHz)')
plt.scatter(T3,A3,label = 'May 24 (476 kHz)')
plt.scatter(T4,A4,label = 'July 5 (1.5975 MHz)',marker='x')
plt.scatter(T5,A5,label = 'July 14 (1.5975 MHz)',marker='x')
plt.scatter(T6,A6,label = 'July 19 (1.5975 MHz)',marker='x')
plt.xlabel('Temperature [°C]')
plt.ylabel('Attenuation coefficient [np/cm]')
plt.legend()
plt.grid(True)
plt.show()












