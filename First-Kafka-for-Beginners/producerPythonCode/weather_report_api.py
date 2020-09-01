# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:07:51 2020

@author: "mojtaba@heroleads.com"
"""

import requests

API_KPY = "ccec3353a5c7bcb01b76a23272e909f2"
API_END_POINT = "https://api.openweathermap.org/data/2.5/weather?appid="


def get_data(city_name='Bangkok'):
    URL = API_END_POINT + API_KPY + "&q=" + city_name
    data  = requests.get(URL)
    return data.content



get_data()