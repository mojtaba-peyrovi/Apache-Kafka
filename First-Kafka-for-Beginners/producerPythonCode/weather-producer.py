# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:11:13 2020

@author: "mojtaba@heroleads.com"
"""

from kafka import KafkaProducer
from weather-report-api import get_data
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')



producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer= json_serializer)


if __name__ == "__main__":
    while 1==1:
        weather_data = get_data()
        print(weather_data)
        producer.send('weather-report', weather_data )
        time.sleep(3)