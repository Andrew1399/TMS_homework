import flask
from flask import render_template, url_for
from flask_login import login_required, current_user

main = flask.Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('users/index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('users/profile.html', name=current_user.username)
