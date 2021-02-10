# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CYeyifyugyuGFE&fdisfyisdgvUFe5tf48fksfy79'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tftp:sfishb4D*Fbhsuv@localhost/tftp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # FLASK-MAIL SETTINGS
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'noreply@example.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '25'))
    MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL', False))
    ADMINS = ['noreplay@example.com']