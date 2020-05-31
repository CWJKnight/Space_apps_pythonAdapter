
import serial
import requests
import json
import time
from requests.exceptions import HTTPError
def get_json():
    url="http://dustmo.com/api/sensors"
    params = dict(
    pressure='pressure',
   )
    resp = requests.get(url=url, json=params)
    data = resp.json()
    jsonArray = data['employees']
    i=0
    while i< len(jsonArray):
        i+=1
    value = jsonArray[i-1]['pressure']
    print(value)
    return value
ser = serial.Serial("COM4", 9600)
while True:
    value=get_json()
    #input_value = input('Enter pixel position: ')
    ser.write(value.encode())
    time.sleep(11)

