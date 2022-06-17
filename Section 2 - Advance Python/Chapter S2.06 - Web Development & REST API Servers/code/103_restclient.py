import requests
import json


baseurl = "http://localhost:5000"

task = "{'task' : 'good one'}"

resp = requests.post(baseurl + "/messages", 
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json',
                              'CSRF-TOKEN' : 'Random String'})
if resp.status_code != 200:
    # This means something went wrong.
    print(resp.status_code)
    
else:
    print("Response")
    print(resp.text)

