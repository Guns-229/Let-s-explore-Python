"""."""
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return "<h1>రేమకు స్వాగతం</h1>"


if __name__ == '__main__':
    app.run()
