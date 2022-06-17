import requests
import json


baseurl = "http://localhost:5000"

task = """{
  "products": [
    [
      1,
      "Mayank",
      "Sat, 10 Jul 1976 00:00:00 GMT",
      2
    ],
    [
      2,
      "sdf",
      "Thu, 30 Dec 2010 00:00:00 GMT",
      33
    ]
  ]
}"""

resp = requests.post(baseurl + "/persons",
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json',
                              'CSRF-TOKEN' : 'Random String'})
if resp.status_code != 200:
    # This means something went wrong.
    print(resp.status_code)
else:
    print("Response")
    print(resp.text)
    print(resp.headers)
    print(resp.json())
