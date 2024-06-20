from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv
from dotenv import load_dotenv
from flask_caching import Cache

from whiteboardassistant.blueprints import user_blueprint, session_blueprint

load_dotenv()

web_app = Flask(__name__)

web_app.config['SECRET_KEY'] = getenv('SECRET_KEY')
web_app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
web_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cache_handler = Cache(web_app)

db_manager = SQLAlchemy(web_app)
db_migration_handler = Migrate(web_app, db_manager)

from whiteboardassistant.models import User, Session

web_app.register_blueprint(user_blueprint, url_prefix='/users')
web_app.register_blueprint(session_blueprint, url_prefix='/sessions')

if __name__ == "__main__":
    web_app.run(debug=True)

@web_app.route('/expensive_computation')
@cache_handler.memoize(timeout=50)
def compute_expensive_operation():
    result = perform_expensive_computation()
    return result

def perform_expensive_computation():
    return "Expensive result"