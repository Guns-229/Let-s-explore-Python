from flask import Flask, jsonify, request
import flask_sqlalchemy


# Create the Flask application and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/cities.sqlite'
db = flask_sqlalchemy.SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    STCode = db.Column(db.String)
    DTCode = db.Column(db.String)
    DTName = db.Column(db.String)
    SDTCode = db.Column(db.String)
    SDTName = db.Column(db.String)
    TVCode = db.Column(db.String)
    Name = db.Column(db.String)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    birth_date = db.Column(db.Date)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    

@app.route('/cities', methods=['GET'])
def getCities():  
    data = City.query.all() #fetch all cities from db
    data_all = []
    for city in data:
        data_all.append([city.id, city.Name, city.SDTName, city.TVCode]) 
    return jsonify(products=data_all)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)