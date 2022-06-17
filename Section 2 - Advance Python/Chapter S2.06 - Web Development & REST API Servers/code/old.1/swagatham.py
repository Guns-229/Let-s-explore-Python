"""."""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return "రేమకు స్వాగతం"


if __name__ == '__main__':
    app.run()
