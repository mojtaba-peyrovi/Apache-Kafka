# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:07:51 2020

@author: "mojtaba@heroleads.com"
"""

import requests

def get_data():

    data  = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=ccec3353a5c7bcb01b76a23272e909f2')
    return data.content
    ss