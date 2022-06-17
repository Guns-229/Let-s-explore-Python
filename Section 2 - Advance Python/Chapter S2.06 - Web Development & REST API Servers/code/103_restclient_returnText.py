import requests
#import json


baseurl = "http://localhost:5000"

task = u"{'task' : 'good one'}"

resp = requests.post(baseurl + "/messages", 
                     data=task,
                     headers={'Content-Type':'text/plain',
                              'CSRF-TOKEN' : 'Random String'})
if resp.status_code != 200:
    # This means something went wrong.
    print(resp.status_code)
    
else:
    print("Response")
    print(resp.text)

