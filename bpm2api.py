import temperature_sensor
import json
import pulse_sensor
import network
import motion_sensor
import urequests
import network
import time


# create WiFi station interface
sta_if = network.WLAN(network.STA_IF)

# activate station interface and connect to WiFi network
sta_if.active(True)
sta_if.connect("SSID", "Password")

# wait for connection
while not sta_if.isconnected():
    pass

print('WiFi connection established')


# Define endpoint URL
url = "url goes here!"

# Read sensor data
while True:
    

    pulse = pulse_sensor.read()


    data = {"pulse": pulse} 

    # Convert data to JSON format
    json_data = json.dumps(data)
    #print(json_data)
    # Set headers
    headers = {"Content-Type": "application/json"}

    # Send HTTP POST request with data and headers
    response = urequests.post(url, data=json_data)
   

    # Print response
    print(response.status_code)
    print(response.text)
    
    time.sleep(10)




