import json

js = '{"task": "add"}'
po = json.loads(js)
print(po, type(po))
