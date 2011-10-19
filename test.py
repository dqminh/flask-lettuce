# -*- coding:utf-8 -*-
import unittest
from flaskext.lettuce import Harvest

class LettuceTest(unittest.TestCase):

    def SetUp(self):
        from flask import Flask
        self.app = Flask(__name__)

    def test_options(self):
        harvest = Harvest(lambda: self.app, start_dir="/home", pattern="*/test")
        options = harvest.get_options()
        self.assertEqual(len(options), 3)
        self.assertEqual(options[0].kwargs['dest'], "verbosity")
        self.assertEqual(options[1].kwargs['dest'], "pattern")
        self.assertEqual(options[2].kwargs['dest'], "start_dir")

if __name__ == "__main__":
    unittest.main()
