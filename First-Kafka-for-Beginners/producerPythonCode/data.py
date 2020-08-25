# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:30:01 2020

@author: "mojtaba@heroleads.com"
"""

from faker import Faker

fake = Faker()


def get_registered_user():
    return {
        'name' : fake.name(), 
        'addess' : fake.address(),
        'created_at' : fake.year()
        
        
        }


if __name__ == "__main__":
    print(get_registered_user())