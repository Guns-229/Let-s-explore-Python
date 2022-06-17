""" swagatham_with_dynamic_rules_2.py
Example using add_url_rule."""
from flask import Flask


app = Flask(__name__)


@app.route('/welcome=<language>')
def select_welcome(language):
    rules = {
        'telugu': రేమకు_స్వాగతం,
        'tamil': நல்வரவு,
        'kannada': ಸುಸ್ವಾಗತ
    }
    print(language)
    return rules[language]()


def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    return "రేమకు స్వాగతం"


def நல்வரவு():
    """swagatham in tamil language."""
    return "நல்வரவு"


def ಸುಸ್ವಾಗತ():
    """swagatham in kannada language."""
    return "ಸುಸ್ವಾಗತ"


if __name__ == '__main__':
    app.run()
