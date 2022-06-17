"""."""
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    x = 1/0
    return "<h1>రేమకు స్వాగతం</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
