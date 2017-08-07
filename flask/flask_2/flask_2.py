from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from werkzeug.routing import  BaseConverter
from werkzeug.utils import secure_filename
from flask.ext.script import Manager


from os import  path
class RegxConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegxConverter, self).__init__(url_map)
        self.regex=items[0]

app = Flask(__name__)
app.url_map.converters['regex']=RegxConverter
manager = Manager(app)

@app.route('/')
def hello_world():
    return render_template('index.html',title="welcome to ...")
@app.route('/services')
def services():
    return 'Services'
@app.route('/about')
def about():
    return 'about'

@app.route('/user/<username>')
def user(username):
    return 'User %s' % username
@app.route('/user_id/<int:user_id>')
def user_id(user_id):
    return '数字 %s' % user_id

@app.route('/use/<regex("[a-z]{3}"):usename>')
def use(usename):
    return 'USER  %s' %usename

@app.route('/projects/')
@app.route('/our-works/')
def projects():
    return 'the project page'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        useranem=request.form['useranme']
        password = request.form['password']
    else:
        suername = request.args['username']

    return render_template('login.html',method=request.method)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath,'static/upload')
        f.save(path.join(upload_path,secure_filename(f.filename)))
        return redirect(url_for('upload'))
    return render_template('upload.html')

@app.route('/index')
def index():
    response = make_response(render_template('index.html',title = 'hllo'))
    response.set_cookie('username')
    return response
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
