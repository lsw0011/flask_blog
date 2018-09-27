from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
		

app = Flask(__name__)
app.config['SECRET_KEY'] = '94fa092f521fc561151c4f5c313c0f6f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes