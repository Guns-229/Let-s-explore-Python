# file: 100_restSample.py
# Run Chapter S2.06 - Web Development & REST API Servers/code/flask/swagatham_2.py
# for server

import requests

try:
    r = requests.get("http://localhost:5000/tamil")
    print(r)
    print(r.status_code)
    print(r.text)
    print(r.json())
except Exception as e:
    print(e)
