# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CYeyifyugyuGFE&fdisfyisdgvUFe5tf48fksfy79'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tftp:sfishb4D*Fbhsuv@localhost/tftp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    ADMINS = ['your-email@example.com']