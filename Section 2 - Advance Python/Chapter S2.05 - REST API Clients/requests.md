

```python
import requests
```


```python
endpoint = 'https://raw.githubusercontent.com/rickiepark/python-tutorial/master/tutorial-4/sample.json'
r = requests.get(endpoint)
```


```python
r.status_code
```




    200




```python
r.headers
```




    {'Content-Length': '285', 'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'; sandbox", 'X-Cache-Hits': '0', 'X-Frame-Options': 'deny', 'Access-Control-Allow-Origin': '*', 'X-Served-By': 'cache-ams4140-AMS', 'X-GitHub-Request-Id': '7D8A:2331:98B583:A5FBE6:59F3328C', 'Expires': 'Fri, 27 Oct 2017 13:25:13 GMT', 'X-Fastly-Request-ID': '6feb490ce8d25b7c4b31f43ffd3c17f6439fd3e8', 'Date': 'Fri, 27 Oct 2017 13:20:13 GMT', 'Source-Age': '0', 'X-Cache': 'MISS', 'Accept-Ranges': 'bytes', 'Strict-Transport-Security': 'max-age=31536000', 'Connection': 'keep-alive', 'X-Geo-Block-List': '', 'Via': '1.1 varnish', 'X-Content-Type-Options': 'nosniff', 'Content-Encoding': 'gzip', 'X-Timer': 'S1509110413.026402,VS0,VE125', 'Vary': 'Authorization,Accept-Encoding', 'ETag': '"d2ca30f0a367151e8325dce8f425b35cb93be8d9"', 'Cache-Control': 'max-age=300', 'Content-Type': 'text/plain; charset=utf-8'}




```python
r.text
```




    u'{\n  "data": [{\n    "type": "articles",\n    "id": "1",\n    "attributes": {\n      "title": "JSON API paints my bikeshed!",\n      "body": "The shortest article. Ever.",\n      "created": "2015-05-22T14:56:29.000Z",\n      "updated": "2015-05-22T14:56:28.000Z"\n    },\n    "relationships": {\n      "author": {\n        "data": {"id": "42", "type": "people"}\n      }\n    }\n  }],\n  "included": [\n    {\n      "type": "people",\n      "id": "42",\n      "attributes": {\n        "name": "John",\n        "age": 80,\n        "gender": "male"\n      }\n    }\n  ]\n}'




```python
obj = r.json()
print(obj)
```

    {u'included': [{u'attributes': {u'gender': u'male', u'age': 80, u'name': u'John'}, u'type': u'people', u'id': u'42'}], u'data': [{u'relationships': {u'author': {u'data': {u'type': u'people', u'id': u'42'}}}, u'attributes': {u'body': u'The shortest article. Ever.', u'updated': u'2015-05-22T14:56:28.000Z', u'created': u'2015-05-22T14:56:29.000Z', u'title': u'JSON API paints my bikeshed!'}, u'type': u'articles', u'id': u'1'}]}



```python
print(obj.__class__)
obj

```

    <type 'dict'>





    {u'data': [{u'attributes': {u'body': u'The shortest article. Ever.',
        u'created': u'2015-05-22T14:56:29.000Z',
        u'title': u'JSON API paints my bikeshed!',
        u'updated': u'2015-05-22T14:56:28.000Z'},
       u'id': u'1',
       u'relationships': {u'author': {u'data': {u'id': u'42',
          u'type': u'people'}}},
       u'type': u'articles'}],
     u'included': [{u'attributes': {u'age': 80,
        u'gender': u'male',
        u'name': u'John'},
       u'id': u'42',
       u'type': u'people'}]}




```python
r = requests.post(endpoint, data={'key':'value'})
```


```python
r = requests.get(endpoint, params={'key1': 'value1', 'key2': 'value2'})
```


```python
r.url
```




    'https://raw.githubusercontent.com/rickiepark/python-tutorial/master/tutorial-4/sample.json?key2=value2&key1=value1'




```python
r = requests.get(endpoint, headers={'user-agent': 'my-app/0.0.1'})
```


```python
r = requests.get('https://github.com', timeout=5)
```


```python
r.cookies
```




    <RequestsCookieJar[Cookie(version=0, name='logged_in', value='no', port=None, port_specified=False, domain='.github.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=2140262600, discard=False, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False), Cookie(version=0, name='_gh_sess', value='eyJzZXNzaW9uX2lkIjoiZjg3MjgxNDllNDZmNzJkODg2OGZiOGZkMWE1MmJmMzYiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUwOTExMDYwMDcxOCwiX2NzcmZfdG9rZW4iOiJYYlJCdEhmMXdJbVZRU0d4ZjEyRXltQWpPVGxoR0Fydnc4UDlSbktyaGtzPSJ9--4162b236fee11ffc769c3cc7b42ff4e50d92871c', port=None, port_specified=False, domain='github.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=True, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>




```python
r.cookies.__class__
```




    requests.cookies.RequestsCookieJar




```python
len(r.cookies)
```




    2




```python
r.cookies['_gh_sess']
```




    'eyJzZXNzaW9uX2lkIjoiZjg3MjgxNDllNDZmNzJkODg2OGZiOGZkMWE1MmJmMzYiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUwOTExMDYwMDcxOCwiX2NzcmZfdG9rZW4iOiJYYlJCdEhmMXdJbVZRU0d4ZjEyRXltQWpPVGxoR0Fydnc4UDlSbktyaGtzPSJ9--4162b236fee11ffc769c3cc7b42ff4e50d92871c'




```python
r.cookies['logged_in']
```




    'no'




```python
r.cookies.get_dict()
```




    {'_gh_sess': 'eyJzZXNzaW9uX2lkIjoiZjg3MjgxNDllNDZmNzJkODg2OGZiOGZkMWE1MmJmMzYiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUwOTExMDYwMDcxOCwiX2NzcmZfdG9rZW4iOiJYYlJCdEhmMXdJbVZRU0d4ZjEyRXltQWpPVGxoR0Fydnc4UDlSbktyaGtzPSJ9--4162b236fee11ffc769c3cc7b42ff4e50d92871c',
     'logged_in': 'no'}


