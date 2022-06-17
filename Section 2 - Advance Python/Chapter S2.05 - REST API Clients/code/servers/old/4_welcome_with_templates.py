from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('welcome.html', author=author, name=name)

if __name__ == "__main__":
    app.run()