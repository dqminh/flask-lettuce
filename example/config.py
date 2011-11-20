# -*- coding:utf-8 -*-

class Config(object):
    DEBUG = False
    TESTING = False


class Dev(Config):
    DEBUG = True


class Test(Dev):
    TESTING = True