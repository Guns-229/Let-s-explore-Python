"""."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return render_template('jinja_variable.html', welcome="రేమకు స్వాగతం" )


if __name__ == '__main__':
    app.run()
