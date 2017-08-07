#encoding=utf-8
from flask_script import Manager
from app import app
from models import User

manager = Manager(app)

@manager.command
def save():
    user = User(2,'king')
    user.save()
@manager.command
def query_all():
    users = User.query_all()
    info =[]
    for u in users:
        info.append(u)
        # print(u)
    return info


if  __name__ == '__main__':
    manager.run()