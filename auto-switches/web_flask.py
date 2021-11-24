

# https://help.ifttt.com/hc/en-us/articles/115010230347-Webhooks-service-FAQ
# for the key https://maker.ifttt.com/use/7exmlYuXrRDcUqCFU5eap
# https://maker.ifttt.com/trigger/{event}/with/key/{webhooks_key}



from flask import Flask
from flask import request
import requests
from time import sleep
import socket
import re
import sys

try:
    import BG96final.processor as processor
except:
    import processor as processor



""" Use Flask/Web to see the logs - current battery level and button stautus - while is working """ 
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from flask'

# @app.route('/ifttt', methods=['POST'])
# def handler():
#     username = request.get_data()
#     print(f"Got tweeted by {username}")
#     return "username: "


pload = {"value1": "", "value2": "", "value3": ""}
sensor_data = processor.SensorData()
lower_threshold = 50.0
upper_threshold = 70.0
# name = sensor_data.sensor_data['na'] = socket.gethostname()   # name

url3_turn_on = 'https://maker.ifttt.com/trigger/cycle2-03-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url4_turn_on = 'https://maker.ifttt.com/trigger/cycle2-04-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url5_turn_on = 'https://maker.ifttt.com/trigger/cycle2-05-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url6_turn_on = 'https://maker.ifttt.com/trigger/cycle2-06-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url7_turn_on = 'https://maker.ifttt.com/trigger/cycle2-07-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url8_turn_on = 'https://maker.ifttt.com/trigger/cycle2-08-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url9_turn_on = 'https://maker.ifttt.com/trigger/cycle2-09-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'
url10turn_on = 'https://maker.ifttt.com/trigger/cycle2-10-battery-low/with/key/7exmlYuXrRDcUqCFU5eap'

url3_turn_off = 'https://maker.ifttt.com/trigger/cycle2-03-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url4_turn_off = 'https://maker.ifttt.com/trigger/cycle2-04-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url5_turn_off = 'https://maker.ifttt.com/trigger/cycle2-05-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url6_turn_off = 'https://maker.ifttt.com/trigger/cycle2-06-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url7_turn_off = 'https://maker.ifttt.com/trigger/cycle2-07-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url8_turn_off = 'https://maker.ifttt.com/trigger/cycle2-08-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url9_turn_off = 'https://maker.ifttt.com/trigger/cycle2-09-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'
url10turn_off = 'https://maker.ifttt.com/trigger/cycle2-10-battery-high/with/key/7exmlYuXrRDcUqCFU5eap'

urls_turn_on = [eval(f"url{i}_turn_on") for i in range(3, 11)]
urls_turn_off = [eval(f"url{i}_turn_off") for i in range(3, 11)]


name = socket.gethostname()
sensor_id = re.findall(r'[\-]\d{2}',name)
print("sensor_id", sensor_id)
sys.exit()

url_turn_on = urls_turn_on[sensor_id-3]     # -3 as senors start cycle2-03
url_turn_off = urls_turn_off[sensor_id-3] 

iter = 3
while (iter > 1):
    sensor_data.battery_update_values()
    if sensor_data.sensor_data['bl'] <= lower_threshold:
        r = requests.post(url_turn_on, data=pload)
        print(r.text)
    elif sensor_data.sensor_data['bl'] > upper_threshold:
        r = requests.post(url_turn_off, data=pload)
        print(r.text)
    else:
        print(f"Battery level now is {sensor_data.sensor_data['bl']}; between upper and lower thresholds")
    sleep(10)
    iter -= 1
