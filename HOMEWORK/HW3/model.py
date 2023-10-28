from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.Integer, default=datetime.utcnow)



    def __repr__(self):
        return f'User({self.name})'