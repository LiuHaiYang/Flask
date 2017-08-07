from flask import Flask,request,url_for,render_template,flash,abort
from models import User

app = Flask(__name__)
app.secret_key = '123'


@app.route('/hello')
def hello_world():
    content = "hello "
    return render_template("index.html",content = content)
@app.route('/username')
def username():
    user = User(1,'ocean')
    return render_template("username.html",user = user)
@app.route('/queryuser/<user_id>')
def queryuser(user_id):
    user = None
    if int (user_id ) == 1:
        user = User(1,'ocean')

    return render_template("user_id.html",user = user)

@app.route('/users/<id>')
def user_id(id):
    return 'hello user :' +id
@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user :' +id
@app.route('/query_url')
def query_url():
    return 'query url :'+url_for('query_url')

@app.route('/list')
def user_list():
    users = []
    for i in range(1,11):
        user = User(i,'ocean' + str(i))
        users.append(user)
    return render_template("user_list.html", users = users)

@app.route('/one')
def one():
    return render_template("one_base.html")
@app.route('/two')
def two():
    return render_template("two_base.html")

@app.route('/')
def hello():
    flash("hello ocean")
    return render_template("from.html")
@app.route('/login',methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("please input username")
        return render_template("from.html")
    if not password:
        flash("please input password")
        return render_template("from.html")
    if username == "ocean" and password =="000000":
        flash("login success")
        return render_template("from.html")
    else:
        flash("username or password is wrong")
        return  render_template("from.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/us/<user_id>')
def not_foundd(user_id):
    if int(user_id) == 1:
        return render_template("index.html")
    else:
        abort(404)
if __name__ == '__main__':
    app.run()
