"""."""
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    langs = ['telugu', 'tamil',
             'kannada', 'german',
             'Hebrew']
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        lang = json_data['lang']
        if lang in langs:
            return jsonify({"msg": eval("{lang}()".format(lang=lang))})
        else:
            return jsonify({"msg": ""})
    else:
        return render_template('jinja_for.html',
                               languages=langs)


@app.route('/telugu')
def telugu():
    """swagatham in telugu language."""
    return "రేమకు స్వాగతం"


@app.route('/tamil')
def tamil():
    """swagatham in tamil language."""
    return "நல்வரவு"


@app.route('/kannada')
def kannada():
    """swagatham in kannada language."""
    return "ಸುಸ್ವಾಗತ"


@app.route('/german')
def german():
    """swagatham in german language."""
    return "Willkommen"


@app.route('/Hebrew')
def Hebrew():
    """swagatham in Hebrew language."""
    return "Shalom"


if __name__ == '__main__':
    app.run()
