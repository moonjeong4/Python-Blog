import uuid
from flask import Blueprint, render_template, request, session,  redirect

from models.user import User

signup_bp = Blueprint('signup', __name__)
login_bp = Blueprint('login', __name__)


@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        from passlib.handlers.pbkdf2 import pbkdf2_sha256
        user_dict = {
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": pbkdf2_sha256.hash(request.form.get('password'))
        }
        return User(user_dict).signup()

    else:
        return render_template('signup.html')


@signup_bp.route('/signout')
def signout():
    session.clear();
    return redirect('/')


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User({'name': request.form.get('name'), 'password': request.form.get('password')})
        return user.login()
    else:
        return render_template('login.html')
