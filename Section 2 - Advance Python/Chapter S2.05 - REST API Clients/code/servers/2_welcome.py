from flask import Flask, url_for
from flask import jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/test/articles')
def api_articles():
    return 'List of ' + url_for('hello_world')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(debug=True)
