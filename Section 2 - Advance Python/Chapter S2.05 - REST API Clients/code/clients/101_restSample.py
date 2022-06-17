# file: 101_restSample.py
# Run Chapter S2.06 - Web Development & REST API Servers/code/flask/swagatham_2.py
# for server

import requests
import inspect

try:
    r = requests.get("http://localhost:5000/tamil")
    print(r)
    public_property_names = [method for method in dir(r)
                               if not callable(getattr(r, method))
                                   if not method.startswith('_')]
    public_method_names = [method for method in dir(r)
                               if inspect.ismethod(method)
                                   if not method.startswith('_')]
    for method in public_method_names:
        getattr(r, method)()
    print("***")
    for prop in public_property_names:
        print(prop, "==", str(getattr(r, prop)).strip())
except Exception as e:
    print(e)
