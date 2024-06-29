from flask import Flask, jsonify
from models import User, Note, Drawing  # Assuming models is the name of your file containing the above classes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    # Using joinedload to reduce SQL queries when accessing notes and drawings.
    user = User.query.options(db.joinedload(User.notes), db.joinedload(User.drawings)).get(user_id)
    if user is not None:
        user_data = {
            'username': user.username,
            'email': user.email,
            'notes': [{'title': note.title, 'content': note.content} for note in user.notes],
            'draws': [{'name': drawing.name, 'data': drawing.drawing_data} for drawing in user.drawings]
        }
        return jsonify(user_data)
    else:
        return "User not found", 404