import requests

baseurl = "http://localhost:5000"


resp = requests.post(baseurl + "/echo")
if resp.status_code != 200:
    # This means something went wrong.
    print(resp.status_code)
    
else:
    print("Response")
    print(resp.text)

