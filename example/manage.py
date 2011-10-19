from flaskext.script import Manager
from flaskext.lettuce import Harvest

if __name__ == "__main__":
    import config
    from main import app_factory

    manager = Manager(app_factory())
    manager.add_command("harvest", Harvest(lambda: app_factory(config.Test)))
    manager.run()