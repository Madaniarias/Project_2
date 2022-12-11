import requests
from datetime import datetime

req = requests.get('http://192.168.6.142/readings')
data = req.json()
readings = data['readings'][0]
hum,temp =[],[]
for sample in readings:
    if sample['sensor_id']==5:
        temp.append(sample)
    if sample['sensor_id']==4:
        hum.append(sample)

sample2 = []
for i in hum:
    #START TIME
    if i['datetime'][8:10] =='09' and i['datetime'][11:13] == '21' and int(i['datetime'][14:16]) in range(35,60):
        sample2.append(i)
    elif i['datetime'][8:10] in ['10','11']:
        sample2.append(i)
    #END_TIME
    #elif i['datetime'][8:10] =='11' and int(i['datetime'][11:13]) in range(0,22) and int(i['datetime'][14:16]) in range(0,36):
    #    sample2.append(i)
