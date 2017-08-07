from . import db
class target_rec(db.Document):
    Pin_ID= db.StringField()
    Target_IP= db.StringField()
    Target_ID= db.StringField()
    Target_Access_DT= db.StringField()
    Target_Web_live_long= db.StringField()
    Target_Rec_DT= db.StringField()
    Target_Signal= db.StringField()

class pins_rec(db.Document):
    Pin_ID = db.StringField()
    Users = db.StringField()
    Pin_Live_long = db.StringField()
    Pin_Date_time= db.StringField()