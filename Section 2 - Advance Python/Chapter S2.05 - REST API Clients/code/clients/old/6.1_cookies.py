my_cookie = {
"version":0,
"name":'COOKIE_NAME',
"value":'true',
"port":None,
# "port_specified":False,
"domain":'www.mydomain.com',
# "domain_specified":False,
# "domain_initial_dot":False,
"path":'/',
# "path_specified":True,
"secure":False,
"expires":None,
"discard":True,
"comment":None,
"comment_url":None,
"rest":{},
"rfc2109":False
}

s = requests.Session()
s.cookies.set(**my_cookie)