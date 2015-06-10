from flask import render_template, flash, redirect, request, url_for, g
from flask.ext.login import login_required, login_user, logout_user, current_user
from app import app, login_manager, db
from forms import LoginForm
from models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@login_required
def show_entries():
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
@login_required
def add_entry():
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user, form.remember_me.data)
            flash('You were logged in')
            return redirect(request.args.get('next') or url_for('show_entries'))
        flash('Invalid username of password.')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_entries'))
