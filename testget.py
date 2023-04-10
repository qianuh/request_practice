import json
import requests
url = 'http://hello.org/api/student'
headers = {'user-agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)
print(r.json())
 

