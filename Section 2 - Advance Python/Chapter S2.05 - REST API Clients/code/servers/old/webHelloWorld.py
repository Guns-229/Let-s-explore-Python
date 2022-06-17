from flask import Flask
app = Flask(__name__)


def echo_get(json_data):
    return True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        ret_code = echo_get(request.json())
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE\n"
    return {"result" : ret_code}


if __name__ == '__main__':
    app.run()
