from project import app, db
from project.models import BlogPost
from flask import render_template, redirect, url_for, session, flash, Blueprint
from functools import wraps

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   

def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('users.login'))
    return wrap

@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')


