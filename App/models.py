from app import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f'{self.title} created on {self.date}'

