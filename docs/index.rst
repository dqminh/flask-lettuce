.. Flask-Lettuce documentation master file, created by
   sphinx-quickstart on Tue Jul 26 13:11:25 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-Lettuce's documentation!
=========================================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

About Flask-Lettuce
===================
Flask-Lettuce is used together with Flask-Script. It is actually a new command
for it that makes it easier to invoke lettuce for your writen features.

By default, Flask-Lettuce will load all features in a folder "features/" inside
your project root.

Usage
=====
Considering that your Flask-Script Manager instance is inside a module called
manage.py then:

	# call's lettuce for all your features inside features/ folder.
	python manage.py harvest

In your manage.py, you configure Flask-Lettuce like this:

	# import flask-script and app_factory (from your code) here
	from flask_lettuce import Harvest

	manager = Manager(app_factory())
	manager.add_command("harvest", Harvest(lambda: app_factory(config.Test)))
