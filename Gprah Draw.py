import Ideal_NSA as I_NSA
import matplotlib.pyplot as plt

NSA = []
NSA_Max = -99999.9
NSA_Min = 9999.9
NSA_High = []
NSA_Low = []

Freq = []
range_low = 30
range_hi = 1001
range_step = 1
NSA_range = 10
NSA_tx_height = 3
NSA_polarity = 'V'

for i in range(range_low,range_hi,range_step):
    Current_NSA = I_NSA.an_ideal(NSA_range,NSA_tx_height,i,NSA_polarity)
    NSA.append(Current_NSA)
    if NSA_Max < Current_NSA: NSA_Max = Current_NSA
    if NSA_Min > Current_NSA: NSA_Min = Current_NSA
    Freq.append(i)

#for i in range(30,201):
#    Freq.append(i)

for i in range(len(NSA)):
    NSA_High.append(NSA[i] + 4)
    NSA_Low.append(NSA[i]-4)

plt.figure(figsize=(15,10))
plt.plot(Freq, NSA, color = 'blue', label = 'Ideal NSA')
plt.plot(Freq, NSA_High, color = 'red', label = 'NSA +4', linestyle = 'dotted')
plt.plot(Freq, NSA_Low, color = 'red', label = 'NSA -4', linestyle = 'dashdot')
plt.ylim([NSA_Min-10,NSA_Max+10])
plt.legend()
plt.xlim([range_low, range_hi])
plt.grid()
plt.title("Normalized Site Attenuation")
plt.xlabel("Frequency (MHz)")
plt.ylabel("NSA (dB)")
plt.show()