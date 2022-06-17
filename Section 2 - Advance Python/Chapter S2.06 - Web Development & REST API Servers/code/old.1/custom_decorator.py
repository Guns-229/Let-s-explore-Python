# https://stackoverflow.com/questions/16096211/custom-decorator-in-flask-not-working
import datetime
from functools import wraps

from flask.app import Flask

app = Flask(__name__)
app.secret_key = "askjsdauisduiasduwen349834"
app.config.from_object(__name__)
app.debug = True


def track_time_spent(name):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            start = datetime.datetime.now()
            ret = f(*args, **kwargs)
            delta = datetime.datetime.now() - start
            print(name, "took", delta.total_seconds(), "seconds")
            return ret
        return wrapped
    return decorator


@app.route('/foo')
@track_time_spent('foo')
def foo():
    print("foo")
    return "foo"


@app.route('/bar')
@track_time_spent('bar')
def bar():
    print("bar")
    return "bar"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088)
