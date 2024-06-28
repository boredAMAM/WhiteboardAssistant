from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    notes = db.relationship('Note', backref='author', lazy=True)
    drawings = db.relationship('Drawing', backref='creator', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Note {self.title}>'

class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    drawing_data = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user a_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Drawing {self.name}>'

class Erase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drawing_id = db.Column(db.Integer, db.ForeignKey('drawing.id'), nullable=False)
    erase_data = db.Column(db.Text, nullable=False)
    date_erased = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Erase {self.id}>'