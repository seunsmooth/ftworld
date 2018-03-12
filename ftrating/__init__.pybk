from flask import Flask
from config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_phantom_emoji import PhantomEmoji

app = Flask(__name__)
app.config.from_object(Config)
PhantomEmoji(app)


#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

from app import routes

# models
