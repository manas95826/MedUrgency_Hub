from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    phone = db.Column(db.String(100))
    name = db.Column(db.String(150))
    patientdetail = db.relationship('patientdetails')
    reports = db.relationship('reports')


class patientdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1000))
    emerphone = db.Column(db.String(100))
    aadharno = db.Column(db.String(100))
    bloodgroup = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    disease = db.Column(db.String(100))
    allergies = db.Column(db.String(100))
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    filename = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class hospitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    key = db.Column(db.String(100))

