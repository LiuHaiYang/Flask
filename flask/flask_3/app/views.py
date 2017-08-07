#-*- code:utf-8 -*-
from flask import render_template,request

def init_views(app):
    @app.route('/')
    def hello_world():
        return render_template('index.html',
                               title="Hello world")
    @app.route('/index')
    def index():
        return render_template('index.html',
                               title="<h1>Hello world</h1>",
                               body="## Header2")
    @app.route('/about')
    def about():
        return render_template('index.html',
                               title="<h1>Hello world</h1>",
                               body="## Header2")
    @app.route('/services')
    def services():
        return render_template('index.html',
                               title="<h1>Hello world</h1>",
                               body="## Header2")
    @app.route('/projects')
    def projects():
        return render_template('index.html',
                               title="<h1>Hello world</h1>",
                               body="## Header2")


    @app.template_filter('md')
    def markdown_to_html(txt):
        from markdown import markdown
        return markdown(txt)


    def read_md(filename):
        with open(filename) as md_file:
            content = reduce(lambda  x,y:x+y,md_file.readlines())
        return content.decode('utf-8')
    @app.context_processor
    def inject_methods():
        return dict(read_md=read_md)