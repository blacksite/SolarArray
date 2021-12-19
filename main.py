##!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import random


if __name__ == '__main__':
    # This is the Publisher
    wait_interval = 60
    BROKER_URL = "192.168.1.89"
    BROKER_PORT = 1883

    client = mqtt.Client()
    client.connect(BROKER_URL, BROKER_PORT)
    client.loop_start()

    while True:
        voltage = random.random() * 2000

        try:
            # client.publish("topic/test", "Hello world!")
            client.publish("solar", voltage, qos=1)
            time.sleep(wait_interval)
        except Exception as e:
            client.connect(BROKER_URL, BROKER_PORT)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
