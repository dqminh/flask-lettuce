# -*- coding: utf-8 -*-
from lettuce import step, world

@step(u'I do nothing')
def i_do_nothing(step):
    assert world.client is not None
#    assert False, 'This step must be implemented'