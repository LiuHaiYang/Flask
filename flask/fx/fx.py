from flask import Flask,jsonify,render_template,request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from sqlalchemy import create_engine
from flask_mongoengine import MongoEngine
from model import *
import numpy as np
import pandas as pd


app = Flask(__name__)
app.config['MONGODB_SETTINGS']={
    "host":'202.206.168.139',
    "port":27017,
    "db":'rec'
}
db = MongoEngine(app)
manager = Manager(app)
# db = SQLAlchemy(app)
api = Api(app)
def con():
    pass

@manager.command
def query_user():
    users = target_rec.objects.all()
    for user in users:
        print(user)
    print(len(users))

# class TrackAPI(Resource): #去除信号量为0的数据 / 根据MAC地址查询信息
#     def get(self,id):
#         con = create_engine('mysql+pymysql://root:root@localhost:3306/track1')
#         index_one = ['Target_ID', 'Pin_ID', 'Target_Access_DT', 'Target_Web_live_long', 'Target_Rec_DT',
#                      'Target_Signal']
#         data = pd.read_sql_table('target_rec', con, columns=index_one)
#         data1 = data[data.Target_Signal != '0'][data[data.Target_Signal != '0'].Target_ID == id]
#         return data1.to_json(date_unit='s',date_format='iso')
#
#     def put(self):
#         pass
# api.add_resource(TrackAPI,'/track/<str:id>')


class TrackAPI1(Resource): #获取数据库
    def get(self,source,start,end):
        if source=='target_rec':
            l=[]
            users = target_rec.objects.all()
            for data in users:
                # if pd.to_datetime('data.Target_Access_DT')>pd.to_datetime(start) :
                l.append(data)
            return jsonify(l)
        elif source=='Pins_rec':
            t=[]
            pins = Pins_rec.objects.all()
            for pin in pins:
                t.append(pin)
            return jsonify(t)

api.add_resource(TrackAPI1,'/v1.0/data/input/<string:source>/<string:start>/<string:end>')


class TrackAPI2(Resource):
    def post(self):
        data = pd.DataFrame(request.json)
        data1 = data[data['Target_Signal'] > 0]
        fx = data.groupby([data1['Target_ID'],data1['Pin_ID']]).size()
        ft = fx.unstack().T.fillna(value=0)
        return ft.to_json()

api.add_resource(TrackAPI2, '/v1.0/data/trace')


if __name__ == '__main__':
    manager.run()
