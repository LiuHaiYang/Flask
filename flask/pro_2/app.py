from flask import Flask,jsonify
from flask_script import Manager
import pymongo
from flask.ext.mongoengine import MongoEngine
from flask_restful import Api,Resource
from datetime import timedelta,date
from models import *
app = Flask(__name__)

manager = Manager(app)
api = Api(app)
db = MongoEngine(app)


class TrackAPI(Resource):
    def get(self):
        client = pymongo.MongoClient('202.206.168.139',27017)
        db = client.rec
        info = db.target_rec
        tar_info = info.find()
        p = []
        for i in tar_info:
            p.append(i)
        return jsonify({'tasks':p})

        # if source == 'target_rec':
        #     rec = db.target_rec
        #     l = []
        #     target = rec.find()
        #     for data in target:
        #         l.append(data)
        #     return jsonify({'tasks':l})
        # elif source == 'Pins_rec':
        #     t = []
        #     targets = db.target_re.find({})
        #     for data in targets:
        #         t.append(data)
        #     return jsonify({'tasks': t})
        # else :
        #     print('数据库不存在')

api.add_resource(TrackAPI,'/track')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
