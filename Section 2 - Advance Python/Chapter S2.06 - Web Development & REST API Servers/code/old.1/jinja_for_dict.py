"""."""
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        lang = json_data['lang']
        return jsonify({"msg": eval("{lang}()".format(lang=lang))})
    else:
        return render_template('jinja_for_dict.html',
                               languages={'telugu': 'రేమకు_స్వాగతం',
                                          'tamil' : 'நல்வரவு',
                                          'kannada': 'ಸುಸ್ವಾಗತ',
                                          'german': 'Willkommen',
                                          'Hebrew': 'Shalom'})


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
