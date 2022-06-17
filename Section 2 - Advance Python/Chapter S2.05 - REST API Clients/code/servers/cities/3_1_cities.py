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


@app.route('/add_cities', methods = ['POST'])
def api_message():
    result = False
    if(request.headers['CSRF-TOKEN'] == "12345"):
        print(request.headers['CSRF-TOKEN'])
        if request.headers['Content-Type'] == 'application/json':
            print(request.json)
            cities.append(request.json["city"])
            result = True
        else:
            print("1")
    else:
        print("2")
    return jsonify({"result": result, "cities": cities}), 5000

#
# @app.route('/test/articles')
# def api_articles():
#     return 'List of ' + url_for('hello_world')
#
# @app.route('/articles/<articleid>')
# def api_article(articleid):
#     return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(debug=True, port=8000)
