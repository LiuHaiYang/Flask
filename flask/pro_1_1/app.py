from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from models import *

app = Flask(__name__)
manager = Manager(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:843800695@localhost:3306/flask'
db = SQLAlchemy(app)
@app.route('/',methods=['GET'])
def hello():
    info = User.query_all()
    taske={
        'id' :info[0].id,
        'name':info[0].name,
    }
    return jsonify({'taske':taske})









# @app.route('/',methods=['GET'])
# def hello_world():
#     def query_all():
#         users = User.query.all()
#         info = []
#         for u in users:
#             info.append()
#             print(u)
#         return jsonify({'info':info})
# @app.route('/users/',methods=['POST'])
# def creat_user():
#     user = User.from_json(request.get_json())
#     db.session.add(user)
#     db.session.commit()


if __name__ == '__main__':
    app.run()