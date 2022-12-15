import Adafruit_DHT
import time
import os
import requests
from datetime import datetime

# NEW USER
# new_user = {'username': 'Zelan', 'password':'81105'}
# req = requests.post(url+"/register", json=new_user)
# print(req.json())

# LOG IN USER
# user = {'username': 'Zelan', 'password':'81105'}
# req = requests.post('http://192.168.6.142/login', json=user)
# access_token = req.json()["access_token"]
# print(access_token)
# auth = {"Authorization": f"Bearer {access_token}"}

# NEW SENSORS
# r = requests.get('http://192.168.6.142/sensors', headers=auth)
# data = r.json()
# readings = data['readings'][0]
# for i in readings:
#	if i['location']=='R4D-A':
#		print(i)

# READ
while True:
    user = {'username': 'Zelan', 'password': '81105'}
    req = requests.post('http://192.168.6.142/login', json=user)
    access_token = req.json()["access_token"]
    # print(access_token)
    auth = {"Authorization": f"Bearer {access_token}"}

    f = open("/home/piroku/proj_data.csv", "a")
    pins = [2, 3, 4, 14]
    sensor_id_temp = {2: 452, 3: 465, 4: 464, 14: 466}
    sensor_id_hum = {2: 467, 3: 468, 4: 469, 14: 471}
    hum, temp = [], []
    for i in pins:
        dht1 = Adafruit_DHT.DHT11
        hum1, temp1 = Adafruit_DHT.read(dht1, i)
        while hum1 is None or temp1 is None:
            hum1, temp1 = Adafruit_DHT.read(dht1, i)
        hum.append(hum1)
        temp.append(temp1)

        # UPLOAD IN SERVER
        new_temp_record = {"datetime": datetime.now().isoformat(), "sensor_id": sensor_id_temp[i], "value": temp1}
        r = requests.post('http://192.168.6.142/reading/new', json=new_temp_record, headers=auth)
        print(r.json())

        new_hum_record = {"datetime": datetime.now().isoformat(), "sensor_id": sensor_id_hum[i], "value": hum1}
        r = requests.post('http://192.168.6.142/reading/new', json=new_hum_record, headers=auth)
        print(r.json())
    f.write(
        '{0},{1}C,{2}C,{3}C,{4}C,{5}%,{6}%,{7}%,{8}%\r\n'.format(datetime.now().isoformat(), temp[0], temp[1], temp[2],
                                                                 temp[3], hum[0], hum[1], hum[2], hum[3]))
    time.sleep(300)
