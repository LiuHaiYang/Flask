from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.controller import blog_message
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:843800695@localhost:3306/flask'
db = SQLAlchemy(app)
