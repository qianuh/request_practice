# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:00:28 2023

@author: qianuh
"""
import json
import requests
url = 'http://hello.org/api/student'
head= {'user-agent': 'Mozilla/5.0'}


r = requests.put('http://hello.org/api/student/5', data = {'name':'haa','birthday':'2001-01-05'})
#print(r.text)
print(r.status_code )
print(r.json())
 

