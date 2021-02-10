# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, models, db
from app.models import User
from app.forms import RegistrationForm, LoginForm
from app.email import send_access_link


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    if request.method == 'GET':
        token = request.args.get('token')
        email = request.args.get('email')

        if not token or not email:
            return render_template('index.html', title='Home')
        else:
            user = User.query.filter_by(email=email).first()
            if user is None or not user.check_token(token) or not user.active:
                return redirect(url_for('index'))
            user.click += 1
            db.session.commit()

            login_user(user)
            return render_template('profile.html', title='Profile', user=user)

    return render_template('index.html', title='Home')


@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    return render_template('profile.html', title='Profile', user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.set_token(form.email.data)
        db.session.add(user)
        db.session.commit()
        send_access_link(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('profile.html', title='Profile', user=current_user)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


