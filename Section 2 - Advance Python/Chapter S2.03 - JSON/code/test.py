"""
myList1 = [10,20,30,40]
for i in range(0,len(myList1)):
    print(myList1.pop())



print(myList1)
"""
from jsonschema import validate,Draft7Validator
import jsonschema
import json

def vali_json(json_file, schema_file):
    try:
        with open(json_file) as jdf, open(schema_file) as jsf:
            data = json.load(jdf)
            schema = json.load(jsf)
            errors = Draft7Validator(schema).iter_errors(data)
            print(errors)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


print(vali_json("data.json", "3schema.json"))
