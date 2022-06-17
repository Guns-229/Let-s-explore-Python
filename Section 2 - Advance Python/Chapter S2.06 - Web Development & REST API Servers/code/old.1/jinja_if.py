"""."""
from flask import Flask, request, render_template, url_for, redirect


app = Flask(__name__)
user_data = {
    'mayank': {
        "role": "user",
        "username": "mayankjohri",
        "userid": 1
    },
    'Manish Gupta': {
        "role": "admin",
        "username": "manish_gupta",
        "userid": 2
    },
    'K.V. pauly': {
        "role": "admin",
        "username": "kvpauly",
        "userid": 3
    }
}


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("POST")
        user = request.form['users']
        print(user)
        return render_template('jinja_if_user.html',
                               user_info=user_data.get(user))
    else:
        return render_template('jinja_if.html',
                               users=user_data.keys())


@app.route("/user_info", methods=['POST'])
def user_info(user):
    return render_template('jinja_if_user.html',
                    user_info=user_data.get(user))

if __name__ == '__main__':
    app.run()
