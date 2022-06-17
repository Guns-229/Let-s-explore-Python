from flask import Flask, render_template, request, Response, g, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from functools import wraps
import json


Base = declarative_base()
app = Flask(__name__)
api = Api(app)

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
auth = HTTPBasicAuth()


class Options(Base):
    __tablename__ = 'opts'
    id = Column(Integer, primary_key=True)
    option = Column(String)
    
    quest_id =  Column(Integer, ForeignKey('quests.id'))
    

class Quests(Base):
    __tablename__ = "quests"
    id = Column(Integer, primary_key=True)
    question = Column(String(32), index=True)
    # 0 -> Radio button
    # 1 -> Checkbox
    otype = Column(Integer) 
    options = relationship("Options", backref="options",
                            cascade="all,delete,delete-orphan")
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

#    def generate_auth_token(self, expiration=600):
#        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
#        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
#        s = Serializer(app.config['SECRET_KEY'])
#        try:
#            data   = s.loads(token)
#        except SignatureExpired:
#            return None    # valid token, but expired
#        except BadSignature:
#            return None    # invalid token
#        user = User.query.get(data['id'])
        return True
 

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
#    user = User.verify_auth_token(username_or_token)
#    user = username_or_token 
    if  username_or_token != None:
        # try to authenticate with username/password
        user = session.query(User).filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    else:
        return False
    g.user = user
    return True

#@app.route('/api/users', methods = ['POST'])
class new_user(Resource):
    
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        print(username, password)
        if username is None or password is None:
            abort(400) # missing arguments
        if session.query(User).filter_by(username = username).first() is not None:
            abort(400) # existing user
        user = User(username = username)
        user.hash_password(password)
        session.add(user)
        session.commit()
        return jsonify({'id':user.id})


class Login(Resource):
    def get(self):
        return Response(render_template('login3.html', page="Login"), mimetype='text/html')
    
    def post(self):
        return ({"result": "ok"});
#        flg = verify_password(request.form['username'], request.form['password'])
#        print(request.form)
#        if flg == True:
#            return ({"result": "ok", "resource" : str(Resource)})
#        else:
#            return ({"result": "nok", "resource" : str(Resource)})

from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

# @login_required
class Start_quiz(Resource):
	def get(self):
		quests = session.query(Quests).all()
		quiz = {}
		for q in quests:
		    ans = {}
		    ans["type"] = q.otype
		    for opts in q.options:
		        ans[opts.id] = opts.option
		    d = {}
		    d = {"question" : q.question, "options": ans}
		    quiz[q.id] = d 
		return json.dumps(quiz)
		

api.add_resource(Login, "/login")
api.add_resource(Start_quiz, "/start_quiz")
api.add_resource(new_user, '/api/users')
print("Testing")
engine = create_engine('sqlite:///userlist.sqlite3', echo=False)
Base.metadata.create_all(engine)
print("Tables created .....")
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    app.run(debug=True)
#session = None
##
## Actually setup the Api resource routing here
##
#api.add_resource(LandingPage, "/")

#api.add_resource(Todo, '/todos/<todo_id>')


##if __name__ == '__main__':
#print("Starting")
#engine = create_engine('sqlite:///userlist.sqlite3', echo=False)
#
#print("Tables created .....")
#Session = sessionmaker(bind=engine)
#session = Session()
#Base.metadata.create_all(engine)
#
#if not os.path.exists('userlist.sqlite3'):
#    create_all()
#app.run(debug=True)
