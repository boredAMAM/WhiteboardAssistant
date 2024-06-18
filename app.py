from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv
from dotenv import load_dotenv
from flask_caching import Cache  # Import the Cache class

from whiteboardassistant.blueprints.users import users_blueprint
from whiteboardassistant.blueprints.sessions import sessions_blueprint

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure cache
app.config['CACHE_TYPE'] = 'simple'  # You can choose other types such as 'redis', 'memcached', etc.
cache = Cache(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from whiteboardassistant.models import User, Session

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(sessions_blueprint, url_add_prefix='/Sessions')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/expensive_computation')
@cache.memoize(timeout=50)  # Cache the result for 50 seconds
def expensive_computation():
    # Simulate an expensive or frequently called computation
    result = do_expensive_computation()
    return result

def do_expensive_computation():
    # placeholder for actual computation logic
    return "Expensive result"