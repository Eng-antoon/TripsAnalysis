#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import datetime
import time

# MQTT broker details
broker = 'b-d3aa5422-cb29-4ddb-afd3-9faf531684fe-1.mq.eu-west-3.amazonaws.com'
port = 8883
username = 'illa-prod'
password = 'EDVBSFZkCMunh9y*Tx'

# List of driver IDs
driver_ids = [
    10152, 10314, 10370, 10457, 10977, 13135, 13690, 13691, 13747, 13758, 13765,
    13770, 13796, 13797, 13832, 13906, 14123, 14314, 14741, 1475, 14826, 14968,
    14992, 14996, 15227, 15587, 15589, 15610, 15631, 15722, 15723, 15792, 15995,
    16405, 16407, 16476, 16495, 16573, 16602, 16620, 16644, 16687, 16688, 16703,
    16704, 16718, 16901, 17038, 17043, 17094, 17105, 17106, 17117, 17134, 17139,
    17153, 17165, 17237, 17259, 17267, 17291, 17297, 17304, 17319, 17329, 17335,
    17346, 17380, 17385, 17401, 17402, 17408, 17468, 17471, 17484, 17487, 17505,
    17513, 17521, 17531, 17535, 17542, 17556, 17568, 17594, 17604, 17705, 17739,
    17750, 17765, 17782, 17801, 17818, 2417, 2452, 263, 290, 2911, 4108, 5067,
    5253, 5260, 5488, 5490, 5560, 5747, 5772, 5889, 5973, 6005, 6067, 6074, 6078,
    6160, 6282, 6434, 6486, 6505, 6740, 6741, 6742, 6843, 7255, 7395, 7460, 9658,
    9688, 9691
]

# Define the date range (inclusive)
start_date = datetime.date(2025, 3, 3)
end_date = datetime.date(2025, 3, 16)

def daterange(start, end):
    """Generator yielding dates from start to end (inclusive)."""
    for n in range((end - start).days + 1):
        yield start + datetime.timedelta(n)

# Create and configure the MQTT client
client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set()  # Uses default TLS settings; adjust if necessary

# Connect to the MQTT broker and start the network loop
client.connect(broker, port)
client.loop_start()

# Publish a message for each driver and each date
for driver_id in driver_ids:
    for current_date in daterange(start_date, end_date):
        date_str = current_date.strftime("%Y-%m-%d")
        topic = f"illa/driver/{driver_id}/log_file/ask"
        print(f"Publishing '{date_str}' to topic '{topic}'")
        client.publish(topic, payload=date_str)
        # Optional: add a short delay to avoid flooding the broker
        time.sleep(0.1)

# Cleanup: stop the loop and disconnect the client
client.loop_stop()
client.disconnect()

print("All messages have been published.")
