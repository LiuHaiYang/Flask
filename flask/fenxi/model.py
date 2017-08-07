from fx import db

class target_rec(db.Model):
    __tablename__='target_rec'
    ID=db.Column(db.Integer,primary_key=True)
    Pin_ID=db.Column(db.Integer)
    Target_IP=db.Column(db.String(765))
    Target_ID=db.Column(db.String(765))
    Target_Access_DT=db.Column(db.DateTime)
    Target_Web_live_long=db.Column(db.Integer)
    Target_Rec_DT=db.Column(db.DateTime)
    Target_Signal=db.Column(db.String(765))
