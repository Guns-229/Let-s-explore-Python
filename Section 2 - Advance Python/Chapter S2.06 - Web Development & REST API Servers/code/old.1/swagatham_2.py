"""."""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/telugu')
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return jsonify({'telugu': "రేమకు స్వాగతం"})


@app.route('/tamil')
def நல்வரவு():
    """swagatham in tamil language."""
    return jsonify({'tamil': "நல்வரவு"})


@app.route('/kannada')
def ಸುಸ್ವಾಗತ():
    """swagatham in kannada language."""
    return jsonify({'kannada': "ಸುಸ್ವಾಗತ"})


@app.route('/german')
def Willkommen():
    """swagatham in german language."""
    return jsonify({'german': "Willkommen"})


@app.route('/Hebrew')
def Shalom():
    """swagatham in Hebrew language."""
    return jsonify({'Hebrew': "Shalom"})


@app.route('/gita')
def gita():
    return """शान्ताकारं भुजगशयनं पद्मनाभं सुरेशं
विश्वाधारं गगनसदृशं मेघवर्णं शुभाङ्गम्।
लक्ष्मीकान्तं कमलनयनं योगिभिर्ध्यानगम्यं
वन्दे विष्णु भवभयहरं सर्वलोकैकनाथम्।।"""


if __name__ == '__main__':
    app.run()
