# -*- coding:utf-8 -*-
from lettuce import before, after, world

from main import app_factory


@before.each_scenario
def setup_scenario(feature):
    world.app = app_factory()
    world.client = world.app.test_client()


@after.each_scenario
def teardown_scenario(scenario):
    del world.client
    del world.app