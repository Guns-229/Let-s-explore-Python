from flask import Flask
# from flask.ext.api import status
from flask_sqlalchemy import SQLAlchemy as AL
import sys, json
from flask import request
from mj_utils import rand_text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'
db = AL(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, index=True, nullable=False)
    password = db.Column(db.String)

    def change_password(self, passwd):
        self.password = passwd

# use only once to create the db and not again.
def create_db():
    db.create_all()


@app.route('/add_user', methods = ['POST'])
def add_user():
    if not request.json:
        abort(400)
    try:
        print(request.json, file=sys.stderr)
        req = request.json
        u = User(name=req["user"], password=rand_text())
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        return json.dumps({"result" : 'nok', "msg": str(e)}), 501
    return json.dumps({'result': 'ok'})


if __name__ ==  "__main__":
    # create_db()
    app.run(debug=True)
