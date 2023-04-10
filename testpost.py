
import json
import requests
url = 'http://hello.org/api/student'
head= {'user-agent': 'Mozilla/5.0'}



r = requests.post('http://hello.org/api/student', data = {'name':'amy','birthday':'2002-03-03'})
#print(r.text)
print(r.json()) 
 

