# variable_rules_2.py

from flask import Flask
from random import randint, uniform

app = Flask(__name__)


@app.route('/get_rand:<int:num>')
def get_random_int(num):
    print("get_random_int", num)
    return str(randint(1, int(num)))


@app.route('/get_rand:<float:num>')
def get_random_float(num):
    print(num)
    return str(uniform(0, float(num)))


@app.route("/get_rand:<num>")
def get_any_rand(num):
    """Every <num> except of data type int & float are handled here"""
    return "not found"


if __name__ == '__main__':
    app.run()
