#-*- code:utf-8 -*-
from flask import Flask
from werkzeug.routing import  BaseConverter
from os import path
from flask_bootstrap import  Bootstrap
from flask_nav import Nav
from flask_nav.elements import  *
from flask_sqlalchemy import SQLAlchemy
from .views import init_views

class RegxConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegxConverter, self).__init__(url_map)
        self.regex=items[0]

basedir = path.abspath(path.dirname(__file__))
bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy
def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegxConverter
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite://'+ path.join(basedir,'date.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

    nav.register_element('top', Navbar(u'Flask入门',
                                       View(u'主页', 'index'),
                                       View(u'关于', 'about'),
                                       View(u'服务', 'services'),
                                       View(u'项目', 'projects'),
                                       ))
    db.init_app(app)
    bootstrap.init_app(app)
    nav.init_app(app)
    init_views(app)
    return app






