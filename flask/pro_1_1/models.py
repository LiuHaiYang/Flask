from app import db

class User(db.Model):
    __tatlename__='user'
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(50))

    class id:
        verbose_name = 'id'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.name)
    # def to_json(self):
    #     json_user={
    #         'user_id ':self.user_id,
    #         'user_name': self.user_name,
    #     }
    #     return json_user
    # @staticmethod
    # def from_json(json_date):
    #     user = User(
    #         user_name = json_date.get('user_name'),
    #         user_id = json_date.get('user_id')
    #     )
    #     return user