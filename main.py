##!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import random


if __name__ == '__main__':
    # This is the Publisher
    wait_interval = 60

    while True:
        voltage = random.random() * 2000

        client = mqtt.Client()
        client.connect("192.168.1.59", 1883, 60)
        # client.publish("topic/test", "Hello world!")
        client.publish("solar", voltage)
        client.disconnect()
        time.sleep(wait_interval)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
