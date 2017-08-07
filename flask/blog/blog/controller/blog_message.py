from blog.model.User import  User
from blog.model.Info import Info
import  os
from blog import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,globals

@app.route('/')
def info():
    info = Info.query.all()
    return render_template('info.html',info)

@app.route('/add',methods=['Post'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    content = request.form['text']
    info = Info(title,content)
    db.session.add(info)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('info'))

@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=request.form['username']).first()
        passwd = User.query.filter_by(password=request.form['password']).first()
        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)
@ app.route('/logout')

def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


