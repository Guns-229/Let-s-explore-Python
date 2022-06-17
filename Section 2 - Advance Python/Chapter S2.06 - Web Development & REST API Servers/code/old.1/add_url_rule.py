"""Example using add_url_rule."""
from flask import Flask

rules = {
    'telugu': రేమకు_స్వాగతం,
    'tamil': நல்வரவு,
    'kannada': ಸುಸ್ವಾಗತ
}

app = Flask(__name__)
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

    for rule, func in rules.items():
        print(rule, func)
        app.add_url_rule('/' + rule, None, func)
    app.run()