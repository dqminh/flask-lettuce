from flaskext.script import Manager
from flaskext.lettuce import Harvest

if __name__ == "__main__":
    from main import app_factory
    manager = Manager(app_factory())
    manager.add_command("harvest", Harvest(app_factory))
    manager.run()