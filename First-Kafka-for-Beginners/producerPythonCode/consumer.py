# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:10:52 2020

@author: "mojtaba@heroleads.com"
"""
from kafka import KafkaConsumer
import json
import json,time
from xlutils.copy import copy    
from xlrd import open_workbook
import pandas




if __name__ == "__main__":
    consumer = KafkaConsumer("registered_user", 
                             bootstrap_servers='localhost:9092', 
                             auto_offset_reset='earliest',
                             group_id='counsmer_group_a')
    print('starting the consumer...')
    for msg in consumer:
        print('registered user: {}'.format(json.loads(msg.value)))


    msg_buffer = []
    buffer_size = 100
    for msg in consumer:
            msg_buffer.append(msg[6])
            if len(msg_buffer) >= buffer_size:
                # book_ro = open_workbook("twitter.xls")
                # book = copy(book_ro)  # creates a writeable copy
                # for _msg in msg_buffer:
                #     sheet1 = book.get_sheet(0)  # get a first sheet
                #     sheet1.write(rowx,colx, _msg)
                # book.save("twitter.xls")
                # msg_buffer = [] 
                with open('sample.txt', 'a') as f:
                    f.write(msg)
                
                
                