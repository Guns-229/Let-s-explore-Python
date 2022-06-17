"""."""
from flask import Flask
from flask import abort, redirect, url_for

app = Flask(__name__)


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


@app.route('/english')
def english():
    """swagatham in english language, but it will abort."""
    abort(404)

@app.route('/welcome:<language>')
def welcome(language):
    return redirect(url_for(language.lower()))


@app.route('/wel:<language>')
def wel(language):
    return redirect("/" + language.lower())


if __name__ == '__main__':
    app.run()
