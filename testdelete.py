import json
import requests
url = 'http://hello.org/api/student'
head= {'user-agent': 'Mozilla/5.0'}


r = requests.delete('http://hello.org/api/student/8/')
#print(r.text)
print(r.status_code )
 
