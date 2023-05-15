from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_caching import Cache

# Initialize Flask app
app = Flask(__name__)

# Load the configuration
app.config.from_object('config.Config')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Redis
redis_store = FlaskRedis(app)

# Initialize Cache
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'  # Replace with your Redis server details if needed
cache = Cache(app)

# Import routes after initializing components to avoid circular imports
from app import routes
