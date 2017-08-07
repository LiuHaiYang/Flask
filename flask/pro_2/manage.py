#encoding= utf-8
from flask_script import Manager
from app import app
from models import Pins_rec

manager = Manager(app)

@manager.command
def query_tar():
    users = Pins_rec.query_target()
    for user in users:
        print(user)


if __name__ == '__main__':
    manager.run()