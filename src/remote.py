import matplotlib.pyplot as plt
import requests
import numpy as np
import warnings
warnings.simplefilter('ignore')

req = requests.get('http://192.168.6.142/readings')
data = req.json()
readings = data['readings'][0]
hum,temp =[],[]

for sample in readings:
    if sample['sensor_id']==5:
        temp.append(sample)
    if sample['sensor_id']==4:
        hum.append(sample)

def times(hum): #GETS THE SPECIFIC TIMES THE LOCAL SERVER ALSO STARTED RECORDING
    sample2 = []
    for i in hum:
    #START TIME
        if i['datetime'][8:10] =='09' and i['datetime'][11:13] == '21' and int(i['datetime'][14:16]) in range(35,60):
            sample2.append(i['value'])
        elif i['datetime'][8:10] in ['10','11']:
            sample2.append(i['value'])
    #END_TIME
    #elif i['datetime'][8:10] =='11' and int(i['datetime'][11:13]) in range(0,22) and int(i['datetime'][14:16]) in range(0,36):
    #    sample2.append(i)
    return sample2

hum = times(hum)
temp = times(temp)
#fig = plt.figure((5,7))

#MOVING AVERAGE SMOOTHING
window=12 #WINDOW IS 12 SO THAT EVERY POINT IS A SUMMARY OF THE TEMP & HUMIDITY PER HOUR
def smoothing(data,window):
    data_ma_mph = []
    data_ma_sth = []
    for t in range(0,len(data),window):
        t_hour = data[t:t+window]
        data_ma_mph.append(sum(t_hour) / len(t_hour))
        data_ma_sth.append(np.std(t_hour))
    return data_ma_mph, data_ma_sth

#x = np.arange(0,len(temp)+1,4)
#print(x)

print(len(hum))
print(len(smoothing(hum,window)[0]))
plt.subplot(3,2,1)
plt.plot(hum)
plt.title('Humidity')
plt.ylabel('Humidity')
lbl=[]
for i in range(0,48):
    lbl.append(str(i))
print(lbl)
txs=[]
for i in range():
    txs.append()
print(np.arange(0,len(hum)+11,12))
plt.xticks(labels=lbl)
plt.xlabel('Hours since Dec 9, 9:35pm')

plt.subplot(3,2,2)
plt.title('Humidity Data Smoothed')
plt.plot(np.arange(len(smoothing(hum,window)[0])), smoothing(hum,window)[0])
plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12))
plt.ylabel('Humidity')
plt.xlabel('Hours since Dec 9, 9:35pm')

plt.subplot(3,2,3)
plt.plot(temp)
plt.title('Temperature')
plt.ylabel('Temperature')
plt.xticks(range(0,len(smoothing(temp,window)[0])+1,4))
plt.xlabel('Hours since Dec 9, 9:35pm')

plt.subplot(3,2,4)
plt.title('Temperature Data Smoothed')
plt.ylabel('Temperature')
plt.plot(np.arange(len(smoothing(temp,window)[0])), smoothing(temp,window)[0])
plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12))
plt.xlabel('Hours since Dec 9, 9:35pm')

plt.subplot(3,2,5)
plt.plot(temp, label='Humidity')
plt.plot(hum, label='Temperature')
plt.legend()

plt.subplot(3,2,6)
counts,bins = np.histogram(hum)
plt.stairs(counts,bins,label="Humidity")
counts,bins = np.histogram(temp)
plt.stairs(counts,bins,label="Temperature")
plt.title('Temperature & Humidity Histogram')

plt.legend()
plt.tight_layout()
plt.show()