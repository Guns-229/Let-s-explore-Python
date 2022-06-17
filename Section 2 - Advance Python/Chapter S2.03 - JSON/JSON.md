
# JSON

The json library can parse JSON from either strings or files. The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

## Parsing JSON
Take the following string containing JSON data:


```python
import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

print(type(json_string))
parsed_json = json.loads(json_string)
print(parsed_json)
print(type(parsed_json))
```

    <class 'str'>
    {'first_name': 'Guido', 'last_name': 'Rossum'}
    <class 'dict'>



```python
print(parsed_json['first_name'], parsed_json['last_name'])
```

    Guido Rossum



```python
json_string = '''[{"first_name": "Guido", "last_name":"Rossum"}, 
                  {"first_name": "Venky", "last_name":"kumar"}]'''

print(type(json_string))
parsed_json = json.loads(json_string)
print(parsed_json)
print(type(parsed_json))
```

    <class 'str'>
    [{'first_name': 'Guido', 'last_name': 'Rossum'}, {'first_name': 'Venky', 'last_name': 'kumar'}]
    <class 'list'>



```python
with open("random.json") as f:
    parsed_json = json.loads(f.read())
    print(parsed_json)
    print(type(parsed_json))
```

    {'results': [{'user': {'gender': 'male', 'name': {'title': 'mr', 'first': 'ernest', 'last': 'coleman'}, 'location': {'street': '6735 greenhaven ln', 'city': 'sunnyvale', 'state': 'connecticut', 'zip': '33332'}, 'email': 'ernest.coleman20@example.com', 'username': 'yellowdog409', 'password': 'ledzep', 'salt': '7iDblTIm', 'md5': '3c9871f954d86c58d3f49b98a7fb60c3', 'sha1': 'd6cb9b8abb27f9718ee9185b2cde298665a177b5', 'sha256': '4fdb19e71c66c91f27f5208cc2a59ca8833ed9b72c549f11ea6a881ffde23c65', 'registered': '1315463131', 'dob': '468664323', 'phone': '(348)-196-2669', 'cell': '(757)-671-8341', 'SSN': '641-99-7751', 'picture': {'large': 'http://api.randomuser.me/portraits/men/72.jpg', 'medium': 'http://api.randomuser.me/portraits/med/men/44.jpg', 'thumbnail': 'http://api.randomuser.me/portraits/thumb/men/47.jpg'}, 'version': '0.6', 'nationality': 'US'}, 'seed': '369a24e79c2f8676'}]}
    <class 'dict'>


## Updated example


```python
d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}

data = json.dumps(d)
print(data)
print(type(data))
```

    {"second_name": "Rossum", "titles": ["BDFL", "Developer"], "first_name": "Guido"}
    <class 'str'>



```python
d = ["mayank", "Venky", "Prashant Bhandarkar"]

data = json.dumps(d)
print(data)
print(type(data))
```

    ["mayank", "Venky", "Prashant Bhandarkar"]
    <class 'str'>


## Examples


```python
### 
import json  
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},  
           "102":{"class":'V', "Name":'David',  "Roll_no":8},  
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}  
print(json.dumps(student)) 
```

    {"102": {"Roll_no": 8, "class": "V", "Name": "David"}, "103": {"Roll_no": 12, "class": "V", "Name": "Samiya"}, "101": {"Roll_no": 7, "class": "V", "Name": "Rohit"}}



```python
import json  
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},  
           "102":{"class":'V', "Name":'David',  "Roll_no":8},  
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}  
print(json.dumps(student, sort_keys=True)); 
```

    {"101": {"Name": "Rohit", "Roll_no": 7, "class": "V"}, "102": {"Name": "David", "Roll_no": 8, "class": "V"}, "103": {"Name": "Samiya", "Roll_no": 12, "class": "V"}}



```python
import json  
tup1 = 'Red', 'Black', 'White';  
print(json.dumps(tup1));
```

    ["Red", "Black", "White"]



```python
import json  
list1 = [5, 12, 13, 14];  
print(json.dumps(list1));
```

    [5, 12, 13, 14]



```python
import json  
string1 = 'Python and JSON';  
print(json.dumps(string1));
```

    "Python and JSON"



```python
import json  
x = True;  
print(json.dumps(x));  
```

    true



```python
import json  
json_data = '{"103": {"class": "V", "Name": "Samiya", "Roll_n": 12}, "102": {"class": "V", "Name": "David", "Roll_no": 8}, "101": {"class": "V", "Name": "Rohit", "Roll_no": 7}}';  
print(json.loads(json_data));

```

    {'101': {'class': 'V', 'Name': 'Rohit', 'Roll_no': 7}, '102': {'class': 'V', 'Name': 'David', 'Roll_no': 8}, '103': {'class': 'V', 'Name': 'Samiya', 'Roll_n': 12}}

