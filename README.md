![weather project](https://user-images.githubusercontent.com/111761417/203182271-24e1b47f-d14d-44fc-bc65-976773cf2baf.gif)

# Unit 2: A Distributed Weather Station for ISAK

**Table of Contents**
1. [Criteria A: Planning](#criteria-a-planning)
   * [Problem definition](#problem-definition)
   * [Proposed Solution](#proposed-solution)
   * [Design statement](#design-statement)
   * [Success Criteria](#success-criteria)
1. [Criteria B: Design](#criteria-b-design)
    * [Record of Tasks](#record-of-tasks)
    * * [Test Plan](#test-plan)
1. [Criteria C: Development](#criteria-c-development)
   * [Existing Tools](#existing-tools)
   * [Techniques Applied](#techniques-applied)
   * [Sources](#sources)
   * [Computational Thinking](#computational-thinking)
   * [Local Server Plots](#local-server-located-in-r4-down-room)
     * [Raw Data Plotting + Average Temperature](#raw-data-plotting--average-temperature)
     * [Raw Data Plotting + Average Humidity](#raw-data-plotting--average-humidity)
     * [Maximum and Minimum + STD Error Bars](#maximum-and-minimum--standard-deviation-error-bars)
   * [Remote Server](#remote-server)
     * [Humidity & Temperature Raw Data Plotting](#humidity--temperature-raw-data-plotting)
     * [Maximum and Minimum for Humidity ]
   * []
2. [Criteria D: Functionality](#criteria-d-functionality)
   * [Science Poster](#science-poster)
   * [Video](#video)

## Criteria A: Planning

## Problem definition

The head of a local school in Japan is interested in maintaining safe levels of humidity and temperature inside and outisde the residences. The school has started to measure manually the levels of humidity and temperature inside each room and outside the residence, however at the moment this method has become too time consuming and tedious to keep track off. It is also difficult for the head of school to maintain organizaed and analyze the data in an efficient manner. The school is in need of a low cost sensing device for humidity and temperature and a custom data script that processes and analyzes the samples acquired.

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

## Design statement

We will design and make a embeded system capable of measure the levels of humidity and temperature for a client who is the head of a local school in Japan. The project will be about designing a low cost sensing device for humidity and temperature and a custom data script that processes and analyzes the samples acquired and will ber constructed using the software Python 3.10.7. It will take about 3 weeks to make and will be evaluated according to the criteria below.

## Success Criteria

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 4 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server.
5. Create a prediction the subsequent 12 hours for both temperature and humidity.
6. A poster summarizing the visual representations, model and analysis is created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

# Criteria B: Design

![](sysdim_hl.png)
![IMG_0128](https://user-images.githubusercontent.com/111761417/206886103-2d6fb313-4914-4985-910a-ecd367ed9be4.jpg)

**Fig.2** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). (Optional) Data from the local raspberry is downloaded to the laptop for analysis and processing.


## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1      | Write the Problem context          |     Establish in a clear and consice manner the problem identified, what is causing the porblem, who is the client and what would the client want that could indicate a posible solution     | 10min                  | Nov 22. | A
| 2      | Write the Desing statement.      | Explain in a consice and clear manner the purpose of the project to the client         | 5min  | Dec 1 | A
| 3      | Draw system diagram for inside the room | To have a clear idea of the hardware and software requirements for the proposed solution for the inisde the room setting | 10min| Dec 1 | B
| 4      | Draw system diagram for outside the residence | To have a clear idea of the hardware and software requirements for the proposed solution for the outside the residence setting | 10min | De 1 | B
| 5      | Build MVP (minimun valuable product) | Set up Raspberry Pi on local desktop & VNC (virtual cloud network) |  30min. | Dec 3. | C
| 6      | Alpha Coding MVP (minimun valuable product) | Code the prototype to collect data from the sensors and print it to the terminal | 30min | Dec 3 | C
| 7      | MVP Testing (Alpha Testing) | Test if the prototype collects data from the sensors and print it to the terminal | 5min. | Dec 3 | C
| 8      | Assemble Embedded System Wiring | Complete set up of four DHT11 sensors on breadboard & raspberry pi with long wires able to reach all around the room | 5 min | Dec 6 | B |
| 9      | Setup remote development with Visual Studio Code | Remote Development enables a programmer to connect to a remote server, in this case the Raspberry Pi, access this server's storage, and work on coding seamlessly as if these files were saved in the programmer's desktop locally [^8]. | 30 minutes | Dec 7 | B 
| 10     | Beta Coding | Write lines of code in Python that enables the Raspberry pi to read data from the four DHT11 sensors set up, upload these data to the [UWC ISAK Japan Weather Station Server]('192.168.6.142'), and save these data in a CSV file in the Raspoberry Pi' storage. | 5 hours | Dec 7 - 9 | C 
| 11      | Alpha-Testig | Allow the Raspberry Pi to collect data, save these data locally in an assigned CSV file, and upload these data to the server. | 40 minutes | Dec 9 | D 
| 12     | Data Collection | Allow the embedded system - Raspberry Pi and its four DHT11 sensors - to collect temperature and humidity data in R4 Down Room A. | 48 hours | Dec 9 10pm to Dec 11 10pm | D 
| 13    | Making mean graphs | Create a piece of code that is able to plot the mean for the temperature and humidity graphs for inside and outside the room separately| 30 min. | Dec 11 | C
| 14    | Making median graphs | Create a piece of code that is able to plot the median for the temperature and humidity graphs for inside and outside the room separately| 30 min. | Dec 11 | C
| 15    | Making Standard deviation graphs | Create a piece of code that is able to plot the standard deviation for the temperature and humidity graphs for inside and outside the room separately | 30 min. | Dec 11 | C
| 16    | Making maximum and minimum graphs | Create a piece of code that is able to plot the maximum and minimum for the temperature and humidity graphs for inside and outside the room separately| 30 min. | Dec 12 | C
| 17    | Making comparison graphs for the means of temperature inside and outside | Create a piece of code that is able to plot the comparison graphs for the temperature inside and outside the room | 30 min. | Dec 12 | C
| 18    | Making comparison graphs for the means of humidity inside and outside | Create a piece of code that is able to plot the comparison graphs for the humidity inside and outside the room | 30 min. | Dec 12 | C
| 19.   | Creating non-linear model for comparison graphs | After analysing the comparison graphs of the mean of the temperature from inside and outside and the the comparison graph of the mean of the humidity from inside and otside, use a non-linear model to create a realtion between the data from inside and outside | 45 min | Dec 12 | C
| 20.  | Alpha-Testig | Run the code for the graphs and identify possible errors to improve the code | 25 min | Dec 12 | C
| 21.  | Creating science poster | Summarizing in a science poster the results obtained from the data plotting: identify methods, reach conclusions and establish recommendations for improvement | 1 hour. | Dec 12 | D
| 22   | Filming explanation videos | Creating a video about the functionality of the code, the explanation and analysis of the results and presentation of the scientific poster and graphs | 1 hour | Dec 12 | D

## Flow Diagrams

### ACCESSING DATA

![Diagrams Cs Project 2-2](https://user-images.githubusercontent.com/111761417/207186556-22b2b4cb-5665-4f2c-9154-732065d628f3.jpg)
**Fig 3.**　The figure shows  the flow diagram used to access the data from the server

### EXPLANATION OF ACCESING DATA

![Diagrams Cs Project 2-3 (1)](https://user-images.githubusercontent.com/111761417/207186937-1e3ec6c0-0bc1-4fe0-9af4-95bc42a34133.jpg)
**Fig 4.**　The figure shows the explanation of each step for the flow diagram used to access the data from the server

### GETTING CODE FROM SERVER DATA DURING THE SPECIFIC TIME PERIOD NEEDED

![Diagrams Cs Project 2-4](https://user-images.githubusercontent.com/111761417/207187111-0c35d412-e6cf-439f-a2d6-c72a3633af71.jpg)
**Fig 5.**　The figure shows for the flow diagram used to getting the code from server data during the 48 hours requiered for the project.

### EXPLANATION GETTING CODE FROM SERVER DATA DURING THE SPECIFIC TIME PERIOD NEEDED

![Diagrams Cs Project 2-5](https://user-images.githubusercontent.com/111761417/207187169-9db339d9-b11f-41c5-b238-a157a9909693.jpg)
**Fig 6.**　The figure shows the explanation of each step for the flow diagram used to getting the code from server data during the 48 hours requiered for the project.

### SMOOTHING
![Diagrams Cs Project 2-6](https://user-images.githubusercontent.com/111761417/207658515-14a6dcea-9180-4ddb-b8c8-344169027118.jpg)
**Fig 7.**　The figure shows for the flow diagram used to smooth the data obtained from server data during the 48 hours requiered for the project when plotting graphs. It is also showned the explanation of each step for the flow diagram used to smooth the data obtained from server.

## Test Plan
| Test No | Type of Test                                                |  Date                                                                                               | Procedure | Expected Outcome |  |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Functional: Testing ability of Raspberry Pi to collect data from the server  | Dec 5 | Connect Raspberry Pi to computer > Open terminal of Raspberry Pi > Open Project.py file > run the program Python project.py. | The Raspberry Pi is able to collect the Temperature and Humidity data from the server in intervals of 5 min.                | 
| 2.      | Functional: Testing ability of Raspberry Pi to collect data from the sensors  |  Dec 5 | Connect Raspberry Pi to computer > Open terminal of Raspberry Pi > Open Project.py file > run the program Python project.py. | The Raspberry Pi is able to collect the Temperature and Humidity data from the sensors in intervals of 5 min without printing message error after more than 3 readings| 
| 3.      | Functional: Getting code from server data during specific time recorded started  | Dec 11 | Call function times that will determine if tha data was taken from a specfic time period needed > run the program Python project.py| Getting the reading only for the time period requested (48 hours).  
| 4.      | Non-Functional: Capabilty for the user to understand the humidity and temperature indoor and outdoor graphs independently| Dec 11           | Open project.py > ask the user to run it > see how much does it take the user to figure the graph out.| The user will understand the graph in less than 3 min  | 
|5.       | Non-Functional: Capability for the user to understand the humidity and temperature indoor and outdoor graphs comparison| Dec 11 | Open project.py > ask the user to run it > see how much does it take the user to understand the comparison through the model proposed. | The user will understand the graph in less than 3 min.
|6.       | Non-Functional: Capability for the user to to understand the humidity and temperature prediction graph | Dec 11 | Open project.py > ask the user to run it > see how much does it take the user to understand the prediction for the next 12 subsequent hours. | The user will understand the graph in less than 3 min.

# Criteria C: Development

## Existing Tools

- For loops
- Functions
- While loops
- If statements
- Unicodes (color)
- Libraries: Matplotlib, Numpy, Datetime, Requests, Adafruit_DHT
- Graphical desktop-sharing system: VCN Viewer
- API server
- CVS files
- Pycharm

## Techniques applied

- Matplotlib library for plotting graphs
- Numpy library for mathematical processes and equations
- Using Graphical desktop-sharing system VCN Viewer to work with Raspberry Pi 4
- Logging in to and reading data from an online api server and posting data to it.
- Datetime library to access times
- Requests library to request data from server
- Reading/Appending/writting csv files
- Adafruit_DHT to wrok with Adafruit DHT series sensors
- Plotting graph for median, mean, maximum, minimum, standard deviation and a non linear model using python.
- Smoothing the data form teh graphs to get a easier to understand graph.
- Using dictionaries and keys to store specific data and retrieve it when necessary

## Sources 

## Computational Thinking
**API Requests**
```.py
#NEW USER
new_user = {'username': 'Zelan', 'password':'81105'}
req = requests.post(url+"/register", json=new_user)
print(req.json())

#LOG IN USER
user = {'username': 'Zelan', 'password':'81105'}
req = requests.post('http://192.168.6.142/login', json=user)
access_token = req.json()["access_token"]
print(access_token)
auth = {"Authorization": f"Bearer {access_token}"}

#CHECK NEW SENSORS INFORMATION
r = requests.get('http://192.168.6.142/sensors', headers=auth)
data = r.json()
readings = data['readings'][0]
for i in readings:
	if i['location']=='R4D-A':
		print(i)
```

**Data Smoothing**
```.py
def smoothing(data,window):
    data_ma_mph = []
    data_ma_sth = []
    for t in range(0,len(data),window):
        t_hour = data[t:t+window]
        data_ma_mph.append(sum(t_hour) / len(t_hour))
        data_ma_sth.append(np.std(t_hour))
    return data_ma_mph, data_ma_sth
```

**Quartic Polynomial Fitting**
```.py
def quartic(data):
    x=np.arange(len(data))
    new_y=[]
    a,b,c,d,e = np.polyfit(x,data, 4)
    print(a,b,c,d,e)
    for i in x:
        eq = (a*(i**4))+(b*(i**3))+(c*(i**2))+(d*i)+e
        new_y.append(eq)
    return new_y
```


## Local server (Located in R4-Down Room)

### RAW DATA PLOTTING + AVERAGE (TEMPERATURE)

<img width="520" alt="57E85873-18D3-44CD-8C9B-B96F3752D788" src="https://user-images.githubusercontent.com/111761417/207747011-fc4a9bf0-41b7-415f-b588-dedb583f0c74.png">

**Fig 8.** The following images presents a series of six graphs related to the temperature in the local server. Firstly, the raw data for each sensor was plotted. Aditionally, a graph with all the raw data from each sensor was added to identify the level of disparity amongst the raw data for the tempeture there is for the raw data in the local server. Laslty, the meam temperature of all sensor was plotted.

By Analizing the graphs plotted it can be said that:
- The minimum temperature recorded during the 48 hours data collection period in the local server was around 17.5°C.
- The maximum temperature recorded during the 48 hours data collection period in the local server was around 22°C.
- Sensor 1 and Sensor 3 recorded the highest temperatures (both reaching around 22.5°C) during the 48 hours data collection period in the local server.
- Sensor 2 and Sensor 4 recorded the lowest temperatures (both reaching around 17°C) during the 48 hours data collection period in the local server.
- Sensor 4 recorded the lowest temperatures out of all sensors during the 48 hours data collection period in the local server.

### RAW DATA PLOTTING + AVERAGE (HUMIDITY)

![08F8F5B0-F056-45B2-8AE9-5D3F3C055724](https://user-images.githubusercontent.com/111761417/207749781-5ffec6bf-86fc-43e2-b022-de7193582920.jpeg)

**Fig 9.** The following images presents a series of six graphs related to the humidity in the local server. Firstly, the raw data for each sensor was plotted. Aditionally, a graph with all the raw data from each sensor was added to identify the level of disparity amongst the raw data for the humidity there is for the raw data in the local server. Laslty, the meam humidity of all sensor was plotted.

By Analizing the graphs plotted it can be said that:
- The minimum humidity recorded during the 48 hours data collection period in the local server was around 20%.
- The maximum humidty recorded during the 48 hours data collection period in the local server was 60.5% (removing the outlier pointed out by python that reaches 140% in Sensor 4).
- Sensor 1 and Sensor 4 recorded the highest humidity levels during the 48 hours data collection period in the local server.
- Sensor 3 and Sensor 4 recorded the lowest humidity levels (both reaching around 17°C) during the 48 hours data collection period in the local server.
- Sensor 4 recorded the highest humidity levels out of all sensors during the 48 hours data collection period in the local server reaching 140%, which presents a big level of disparity compared to the rest of the data for humidity, indicating that something might have happened with that sensors duting the 48 data collection period in the local server.

### MAXIMUM AND MINIMUM + STANDARD DEVIATION (ERROR BARS) 

![9953676F-0D99-4284-8297-1E2570517C04](https://user-images.githubusercontent.com/111761417/207796687-b4ac7e3b-de05-489c-956f-e69b67f20d38.jpeg)

**Fig 10.** The following images presents a graph for the smoothed indoor average temperature in the local server. The error bars are based on standard deviation and the minimum and Maximum of all four indoor sensors are shown through the fill.inbetween plot. The smoothing window is 12 beacause the server collects data every 5 minutes.

By Analizing the graphs plotted it can be said that:
- Becuase most of the error bars are overlaping, we can say that the data obtained from all sesors does not differ that much from one another so, consequently, and avergae could be used.


## Remote server

### HUMIDITY & TEMPERATURE RAW DATA PLOTTING

![B6B1D161-BB55-4790-8EE4-BFE5CE2C9951](https://user-images.githubusercontent.com/111761417/207772323-cc870b6e-dfca-4188-9b9e-3e20d534b0b1.jpeg)
**Fig 11.** The following image presents a set of four graphs related to the humidity and temperature in the remote server server. The two graphs on top represent the humidity data collected by the sensor in the remote server during the 48 hour data collection period and, next to it, the grpah for the same data smoothed. Similarly, the two graphs on the bottom represent the temperature data collected by the sensor in the remote server during 48 hour the data collection period and, next to it, the grpah of the same data smoothed.

### MAXIMUM AND MINIMUM FOR HUMIDITY & TEMPERATURE DATA PLOTTING

![3C4720B2-9E54-4215-9CB4-CB2D027E9080](https://user-images.githubusercontent.com/111761417/207792958-f5ce507d-643f-4ec3-acac-7c183ac57056.jpeg)
![D0B9946D-F79F-41C8-A47C-DFE93652071C](https://user-images.githubusercontent.com/111761417/207792370-0053b265-1664-4762-9f75-6c34e7b76d9d.jpeg)

**Fig 12.** The following image presents a set of two graphs for the humidity and temperature maximum and minimum values in the remote server server. The graph on top represents the humidity maximum and minimum values of the data collected by the sensor in the remote server during the 48 hour data collection period outdoors. Similarly, the graph on top represents the temperature maximum and minimum values of the data collected by the sensor in the remote server during the 48 hour data collection period outdoors.

By Analizing the graphs plotted it can be more accuratly determined the maximum and minimum values for temperature and humidity in the remote server:
- The minimum humidity recorded during the 48 hours data collection period in the remote server was 25%.
- The maximum humidty recorded during the 48 hours data collection period in the remote server was 44%.
- The minimum temperature recorded during the 48 hours data collection period in the local server was 13°C.
- The maximum temperature recorded during the 48 hours data collection period in the local server was 26°C.

### MEDIAN FOR TEMPERATURE AND HUMIDITY

![Screen Shot 2022-12-15 at 17 25 00](https://user-images.githubusercontent.com/111761417/207809988-a4001209-0dc5-4282-8337-79a5555a7b4e.png)

**Fig 13.** The following image present a graph for the mean of the temperature in the remote server server during the 48 hour data collection period.

By Analizing the graphs plotted it can be said that:
- The value for the median is 21°C.

![Screen Shot 2022-12-15 at 17 26 36](https://user-images.githubusercontent.com/111761417/207810020-8a1e1f07-76fc-4032-bff4-40910dc8d972.png)

**Fig 14.** The following image present a graph for the mean of the humidity in the remote server server during the 48 hour data collection period.

By Analizing the graphs plotted it can be said that:
- The value for the median is 33%.

## Comparisons between Local and Remote servers

### OUTDOOR VS. INDOOR AVERAGE TEMPERATURE AND HUMIDITY

![D55DEE78-2ECD-4DF5-918F-788145BDACE4](https://user-images.githubusercontent.com/111761417/207812774-9ecb9748-bbcd-4660-a9ff-59408e3e83ee.jpeg)

**Fig 15.** The following image presents a set of two graphs comparing the means of the humidity and temperature in the local server vs the remote sever during the 48 hour data collection period.

By Analizing the graphs plotted it can be said that:
- The temperature inside tended to be lower than outside due to the heaters inside the houses.
- The temperature inside tended to be more consistent than outside because the conditions inside the room where almost the same during the data collection period (windonds closed, same temperature in heater, etc) whereas outside it was more incosistent due to the cnahe in weather conditions (snow, rain, sun, etc)
- The humidity inside the rooma was lower than the humidity outside the room.

### CURVE FIT OUTDOOR TEMPERATURE

![70FFA93E-7CE1-4B2E-B722-E3B3CB610781](https://user-images.githubusercontent.com/111761417/207867607-a57cb26c-3c27-4247-85f7-4964a6778e65.jpeg)

**Fig 16.** The following image presents a graph plotting for the outdoor temperature during the 48 hour data collection period. Three trials were done with the Polynomial model to determine the best fit for the representation of the graph (Deg:3, Deg:4, Deg:5). For matters of this graph, the model for the quartic Polynomial model (Deg: 4) is preferred.

### MODEL INDOOR TEMPERATURE AND HUMIDITY + PREDICTIONS

![32B55420-CCFB-44A5-A9A5-97AF875D39FD](https://user-images.githubusercontent.com/111761417/207895232-58673ae7-deb1-40ac-b88b-334167a8a31a.jpeg)

**Fig 17.** The following image presents a set of graphs for the indoor temperature and humidity during the 48 hour data collection period. A quatric polynomial model was used when plotting the graphs. Additionally, the predictions for the next 12 hours are recorded in the graphs.

# Criteria D: Functionality

## Scientific Poster

![WEATHER STATION](https://user-images.githubusercontent.com/111761417/207924878-5a0bc134-8e29-4610-9041-01204e621488.png)

**Fig 18.** The following image presents the scientific poster for the project. It is divided in 5 section being Background, Methods, Results, Conclusions and Recommendations respectevely.

The Science Poster, Comparative Analysis, and Video/Demo is stored in this Google Drive:
https://drive.google.com/drive/folders/1Kz8aMAfJCHmsgjQVhcB54h2y-usvIOQJ?usp=sharing


[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386.
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata.
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/.
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management.
[^8]: Visual Studio Code Remote Development Frequently Asked Questions. 3 Nov. 2021, code.visualstudio.com/docs/remote/faq/.
