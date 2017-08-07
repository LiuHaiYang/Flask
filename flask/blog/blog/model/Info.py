from blog import db
class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    content = db.Column(db.String(200))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self, username, password):
        return '<Info %r>' % self.title