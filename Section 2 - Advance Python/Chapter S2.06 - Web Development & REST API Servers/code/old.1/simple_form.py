
from flask import Flask, request, render_template

app = Flask(__name__)


def show_login():
  return render_template("login_form.html")

@app.route('/logmein', methods=['GET', 'POST'])
def logmein():
    if request.method == 'POST':
        welcome_str = "Welcome user: {}".format(request.form['username'])
        return welcome_str
    else:
        print("Lets login to the user")
        return render_template("login_form.html")

if __name__ == '__main__':
    app.run()
