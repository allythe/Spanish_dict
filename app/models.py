from flask_login import UserMixin

from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    words = db.relationship('Cidian', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % self.id


class Cidian(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng = db.Column(db.String(100), nullable=False)
    sp = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return self.id

