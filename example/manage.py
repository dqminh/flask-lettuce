from flask.ext.script import Manager
from flask.ext.lettuce import Harvest

if __name__ == "__main__":
    import config
    from main import app_factory

    manager = Manager(app_factory)
    manager.add_option("-c", "--config", dest="config_obj", default=config.Dev, required=False)
    manager.add_command("harvest", Harvest(lambda: app_factory(config.Test)))
    manager.run()