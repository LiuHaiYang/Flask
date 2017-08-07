import pymongo
from app import *
def get_coll():
    client = pymongo.MongoClient('202.206.168.139',27017)
    db = client.rec
    Pins_rec = db.Pins_rec
    return Pins_rec

class target_rec(object):
    def __init__(self,Pin_ID,Target_IP,Target_ID,Target_Access_DT,Target_Web_live_long,Target_Rec_DT,Target_Signal):
        self.Pin_ID = Pin_ID
        self.Target_IP = Target_IP
        self.Target_ID = Target_ID
        self.Target_Access_DT = Target_Access_DT
        self.Target_Web_live_long = Target_Web_live_long
        self.Target_Rec_DT = Target_Rec_DT
        self.Target_Signal = Target_Signal

class Pins_rec(object):
    def __init__(self,Pin_ID,Users,Pin_Live_long,Pin_Date_time):
        self.Pin_ID = Pin_ID
        self.Users = Users
        self.Pin_Live_long = Pin_Live_long
        self.Pin_Date_time = Pin_Date_time
    @staticmethod
    def query_target():
        Pins_rec= get_coll().find()
        return Pins_rec
