# -*- coding: utf-8 -*-
"""
    ~~~~~~~~~~~~

    Implements the configuration related objects.

"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tftp:sfishb4D*Fbhsuv@localhost/tftp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['your-email@example.com']