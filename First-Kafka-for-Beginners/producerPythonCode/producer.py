# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:11:13 2020

@author: "mojtaba@heroleads.com"
"""

from kafka import KafkaProducer
from data import get_registered_user
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')



producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer= json_serializer)


if __name__ == "__main__":
    while 1==1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send('registered_user', registered_user )
        time.sleep(3)