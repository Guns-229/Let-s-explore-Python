import requests
#import json
import json

baseurl = "http://localhost:5000"

urls = {
    "login" : "/login",
    "create" : "/create"
}


def login(username, password):
    payload = json.loads({'username': username, "password", password})
    payload_form = "username={{username}}&password={{password}}.format(
                       username, password) 
     
    resp = requests.post(baseurl + urls['login'], 
                        data = payload_form
                        headers={'Content-Type':'text/json',
                                'CSRF-TOKEN' : 'Random String',
})
    
    if resp.status_code != 200 and "success" in resp.body :
        return True, resp.headers
    else 
        return False, None
        
    # This means something went wrong.
    print(resp.status_code)
    
else:
    print("Response")
    print(resp.text)


if __name__ == "__main__":
    confs = readConfig()
    confs.username
    congs.baseurl
    
