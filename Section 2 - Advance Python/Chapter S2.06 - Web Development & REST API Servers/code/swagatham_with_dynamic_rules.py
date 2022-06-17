"""Example using add_url_rule.

- We are adding tamil, telugu using code before the app is run.
- We are adding kannada at runtime after the server has started.
"""
from flask import Flask


def telugu():
    """swagatham in telugu language."""
    return "రేమకు స్వాగతం"


def tamil():
    """swagatham in tamil language."""
    app.add_url_rule("/kannada", None, kannada)
    return "நல்வரவு"


def kannada():
    """swagatham in kannada language."""
    return "ಸುಸ್ವಾಗತ"


if __name__ == '__main__':
    rules = {
        'telugu': telugu,
        'tamil': tamil,
    }

    app = Flask(__name__)
    for rule, func in rules.items():
        app.add_url_rule('/' + rule, None, func)
    app.run()
