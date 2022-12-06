![weather project](https://user-images.githubusercontent.com/111761417/203182271-24e1b47f-d14d-44fc-bc65-976773cf2baf.gif)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition

The head of a local school in Japan is interested in maintaining safe levels of humidity and temperature inside and outisde the residences. The school has started to measure manually the levels of humidity and temperature inside each room and outside the residence, however at the moment this method has become too time consuming and tedious to keep track off. It is also difficult for the head of school to maintain organizaed and analyze the data in an efficient manner. The school is in need of a low cost sensing device for humidity and temperature and a custom data script that processes and analyzes the samples acquired.

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

**Design statement**

We will design and make a embeded system capable of measure the levels of humidity and temperature for a client who is the head of a local school in Japan. The project will be about designing a low cost sensing device for humidity and temperature and a custom data script that processes and analyzes the samples acquired and will ber constructed using the software Python 3.10.7. It will take about 3 weeks to make and will be evaluated according to the criteria below.

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
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
| 8      | Assemble Embedded System Wiring | Complete set up of four DHT11 sensors on breadboard & raspberry pi with long wires able to reach all around the room | 5 min | Dec 6 | C 


* Code - Create lines of code for the data to be recorded to a CSV file - 10 minutes | Dec 6 
* Setup Raspberry Pi remote development with VS Code | / | 2 hours | Dec 6 | C
* Code - Create lines of code for the data to be sent to the server



## Test Plan

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
