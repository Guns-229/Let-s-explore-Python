
# JSON

The json library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

## Parsing JSON
Take the following string containing JSON data:


```python
import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)
print(parsed_json)
print(type(parsed_json))
```

    {'last_name': 'Rossum', 'first_name': 'Guido'}
    <class 'dict'>
    


```python
print(parsed_json['first_name'], parsed_json['last_name'])
```

    Guido Rossum
    

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

    {"second_name": "Rossum", "first_name": "Guido", "titles": ["BDFL", "Developer"]}
    <class 'str'>
    

## Examples


```python
### 
import json  
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},  
           "102":{"class":'V', "Name":'David',  "Roll_no":8},  
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}  
print(json.dumps(student)); 
```

    {"101": {"class": "V", "Name": "Rohit", "Roll_no": 7}, "102": {"class": "V", "Name": "David", "Roll_no": 8}, "103": {"class": "V", "Name": "Samiya", "Roll_no": 12}}
    


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
    


```python

```
