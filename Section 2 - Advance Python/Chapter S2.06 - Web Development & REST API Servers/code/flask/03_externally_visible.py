""" 03_externally_visible.py"""
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return "రేమకు స్వాగతం"


if __name__ == '__main__':
    app.run(debug=True, port=20202, host="0.0.0.0")

