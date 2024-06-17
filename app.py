from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv
from dotenv import load_dotenv
from whiteboardassistant.blueprints.users import users_blueprint
from whiteboardassistant.blueprints.sessions import sessions_blueprint

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from whiteboardassistant.models import User, Session

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(sessions_blueprint, url_prefix='/Sessions')

if __name__ == "__main__":
    app.run(debug=True)