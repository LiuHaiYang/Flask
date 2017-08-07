from flask import Flask,jsonify,render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask.ext.mongoengine import MongoEngine
from sqlalchemy import create_engine
from model import *
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
app = Flask(__name__)
manager = Manager(app)
db = SQLAlchemy(app)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'host':'202.206.168.139',
    'port':'27017',
    'db':'rec',
}



class UserAPI(Resource):
    def get(self, sourse):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/api/1.0/<string:sourse>', endpoint = 'user')






@app.route('/')
def hello_world():
    tasks = [
        {
            'MAC': 'aaa',
            '101': '10',
            '102': '5',
            '103': '0',
            '104': '0',
            '105': '0',
            '106': '0',
            '107': '10',
            '108': '0',
            '109': '10',
            '110': '5',
            '111': '0',
            '112': '30',
            '114': '0',
            '115': '0',
            '116': '0',
            '118': '0',
            '119':'0',
        },
        {
            'MAC': 'aaa',
            '101': '0',
            '102': '0',
            '103': '0',
            '104': '10',
            '105': '0',
            '106': '0',
            '107': '50',
            '108': '0',
            '109': '10',
            '110': '5',
            '111': '0',
            '112': '0',
            '114': '10',
            '115': '0',
            '116': '0',
            '118': '0',
            '119': '0'
        },
    ]

    return render_template('index.html',tasks=tasks)

if __name__ == '__main__':
    app.run()
