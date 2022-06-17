from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE\n"
        
        
@app.route('/messages', methods = ['POST'])
def api_message():
    if(request.headers['CSRF-TOKEN']):
        print(request.headers['CSRF-TOKEN'])
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + str(request.data)

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"
		
		
if __name__ == '__main__':
    app.run()