import unittest
from flaskext.lettuce import Harvest

class LettuceTest(unittest.TestCase):

    def test_options(self):
        harvest = Harvest(app=None, start_dir="/home", pattern="*/test")
        options = harvest.get_options()
        self.assertEqual(len(options), 3)
        self.assertEqual(options[0].kwargs['dest'], "verbosity")
        self.assertEqual(options[1].kwargs['dest'], "pattern")
        self.assertEqual(options[2].kwargs['dest'], "start_dir")

if __name__ == "__main__":
    unittest.main()
