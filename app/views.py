from flask import render_template, flash, redirect, request, url_for, g
from flask.ext.login import login_required, login_user, logout_user, current_user
from app import app, login_manager,db
from forms import LoginForm, RegistrationForm
from models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@login_required
def show_entries():
    entries = [None]
    return render_template('show_entries.html', entries=entries)

@app.route('/test')
@login_required
def test():
    return 'test'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('show_entries'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname=form.name.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash('You were logged in')
            return redirect(request.args.get('next') or url_for('show_entries'))
        flash('Invalid username of password.')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(nickname=form.name.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
