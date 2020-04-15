from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, session   # pragma: no cover

from flask_login import login_user, login_required, logout_user

from app import app
from flask_bcrypt import Bcrypt
from functools import wraps
# from .forms import LoginForm, RegisterForm   # pragma: no cover
# from project import db   # pragma: no cover
# from project.models import User, bcrypt   # pragma: no cover

bcrypt = Bcrypt(app)
################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   # pragma: no cover

def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap


################
#### routes ####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credential.'
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@users_blueprint.route('/logout')   # pragma: no cover
@login_required   # pragma: no cover
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('welcome'))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)