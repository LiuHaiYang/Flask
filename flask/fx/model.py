#from fx import db

# class Target_rec(object):
#     __tablename__='target_rec'
#     ID=db.Column(db.Integer,primary_key=True)
#     Pin_ID=db.Column(db.Integer)
#     Target_IP=db.Column(db.String(765))
#     Target_ID=db.Column(db.String(765))
#     Target_Access_DT=db.Column(db.DateTime)
#     Target_Web_live_long=db.Column(db.Integer)
#     Target_Rec_DT=db.Column(db.DateTime)
#     Target_Signal=db.Column(db.String(765))
from fx import db


class target_rec(db.Document):
    Pin_ID= db.StringField()
    Target_IP= db.StringField()
    Target_ID= db.StringField()
    Target_Access_DT= db.StringField()
    Target_Web_live_long= db.StringField()
    Target_Rec_DT= db.StringField()
    Target_Signal= db.StringField()


class Pins_rec(db.Document):
    Pin_ID = db.StringField()
    Users = db.StringField()
    Pin_Live_long = db.StringField()
    Pin_Date_time = db.StringField()