from flask import Flask,jsonify
from models import User
# import pymysql
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:843800695@localhost:3306/flask'
# # app.config['SQLALCHEMY_COMMIT_ON_TEAROWN'] = True
# db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/query',methods=['GET','POST'])
def query_all():
    users = User.query_all()
    return users
if __name__ == '__main__':
    app.run()