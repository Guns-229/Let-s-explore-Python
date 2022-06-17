""" 02_route_example.py """
from flask import Flask


app = Flask(__name__)


@app.route('/telugu')
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return "రేమకు స్వాగతం"


@app.route('/tamil')
def நல்வரவு():
    """swagatham in tamil language."""
    return "நல்வரவு"


@app.route('/kannada')
def ಸುಸ್ವಾಗತ():
    """swagatham in kannada language."""
    return "ಸುಸ್ವಾಗತ"


@app.route('/german')
def Willkommen():
    """swagatham in german language."""
    return "Willkommen"


@app.route('/Hebrew')
def Shalom():
    """swagatham in Hebrew language."""
    return "Shalom"


if __name__ == '__main__':
    app.run()
