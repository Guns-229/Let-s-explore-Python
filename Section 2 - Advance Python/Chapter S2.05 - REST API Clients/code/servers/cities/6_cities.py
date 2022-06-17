from flask import Flask, url_for, request
from flask import jsonify


app = Flask(__name__)
cities = [
        "New Delhi", "Chennai", "Bangeluru",
        "Bhopal", "Indore", "Nagpur", "Mumbai"
         ]
@app.route('/cities', methods=['GET'])
def hello_world():
    return jsonify(cities)


@app.route('/cities/<string:name>', methods=['POST'])
def returnOne(name):
    print(request.cookies)
    cities.append(name)
    return jsonify({'result' : True, "cities": cities}), {"12342": "blabla",
                                                          "Set-Cookie": "test='1234'"}

if __name__ == '__main__':
    app.run(debug=True, port=8000)
