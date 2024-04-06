# DocAid

## Project Description 

IoT wearable device made using Arduino and sensors along with complete hospital management support for all the wearables linked through the software. Submitted to Thapar University in 2023 as a capstone project. Works as a prototype for future hospital wearable researches. The IoT device has three sensors and 4 vital reading that ar send to a realtime firebase database, the webapp (developed using Django) then picks these reading and displays them on the patient dashboard that has realtime graphs, doctor comments and patient details.

## Technology used : 

<p align="center">
 <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python" height="50" style="vertical-align:top; margin:4px"></a>
 <a href="https://www.djangoproject.com/"> <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django" height="50" style="vertical-align:top; margin:4px"></a>
  <a href="https://firebase.google.com/"> <img src="https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase" alt="Firebase" height="50" style="vertical-align:top; margin:4px"></a>
  <a href="https://www.arduino.cc/"> <img src="https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" alt="Arduino" height="50" style="vertical-align:top; margin:4px"></a>
</p>

## Hardware used : 

The List of hardware used in the project :

- [`Arduino Uno`](https://docs.arduino.cc/hardware/uno-rev3/) : Brain of the system, used to get signal from all the sensors.
- [`Node MCU`](https://projecthub.arduino.cc/PatelDarshil/getting-started-with-nodemcu-esp8266-on-arduino-ide-b193c3) : ESP8266 Wi-Fi SoC , used to send all the sensor reading to firebase database.
- [`MAX30100`](https://www.electronicwings.com/arduino/max30100-pulse-oximeter-interfacing-with-arduino) : Heart rate and SpO2 meter. Integrated pulse oximetry and heartrate monitor sensor solution.
- [`AD8232`](https://robu.in/ecg-sensor-ad8232-heart-rate-monitor-detail-guide-interfacing-with-arduino/) : ECG module. Integrated signal conditioning block for ECG measurement.
- [`MLX90614`](https://lastminuteengineers.com/mlx90614-ir-temperature-sensor-arduino-tutorial/) : Temperature Module. Infrared thermometer for non-contact temperature measurements.

  
## Circuit Diagram : 

<p align="center">
 <a ><img src="https://github.com/prateek11rai/DocAid/blob/main/circuit_diagram.png" alt="Circuit Diagram" height="500" style="vertical-align:top; margin:4px"></a>
</p>

## UI Screenshots :

<p align="center">
 <a ><img src="https://github.com/prateek11rai/DocAid/blob/main/patient_1.png" alt="Homepage" height="400" style="vertical-align:top; margin:4px"></a>
  <a ><img src="https://github.com/prateek11rai/DocAid/blob/main/patient_2.png" alt="Patient Dashboard" height="500" style="vertical-align:top; margin:4px"></a>
</p>

<br/>
