"""Echo Implementation in flask."""
from flask import Flask, request

app = Flask(__name__)


@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        print(request.form)
        return request.form['echo']
    else:
        return """<html>
        <body>
           <form action="/echo" method="post">
              Text to echo: <input type="text" name="echo"><br>
              <input type="submit" value="Submit">
            </form>
        </body></html>
        """


if __name__ == '__main__':
    app.run(debug=True)
