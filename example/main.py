# -*- coding:utf-8 -*-

import config

from flask import Flask

def app_factory(config_obj=None):
    app = Flask(__name__)
    app.config.from_object(config_obj or config.Dev)
    return app
