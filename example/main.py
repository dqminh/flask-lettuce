# -*- coding:utf-8 -*-

from flask import Flask

def app_factory():
    app = Flask(__name__)
    return app
