# -*- coding: utf-8 -*-
"""
    flaskext.lettuce
    ~~~~~~~~~~~~~~~~

    Add Lettuce support for Flask application

    :copyright: (c) 2011 by Daniel, Dao Quang Minh (dqminh).
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import
import inspect
import fnmatch
import os
from flask import Response, request
from flask.testing import FlaskClient
from flaskext.script import Command, Option
from lettuce import Runner, registry, before, after, world

class TestResponse(Response):
    """A :class:`~flask.Response` adapted to testing, this is returned by
    the test client. The added feature is that it can be compared against
    other response objects."""

    def __eq__(self, other):
        self.freeze()
        other.freeze()
        other.headers[:] = other.get_wsgi_headers(request.environ)
        return all(getattr(self, name) == getattr(other, name)
                   for name in ('status_code', 'headers', 'data'))

    def __ne__(self, other):
        return not self == other


class Harvest(Command):
    """
    Harvest all features of the current application and run them
    """
    def __init__(self, app_factory, pattern='*/features', start_dir=None, verbosity=4):
        if start_dir is None:
            # Find the file that called this constructor and use its directory
            # as the start dir to scan for pattern
            for f in inspect.stack():
                start_dir = os.path.dirname(os.path.abspath(f[1]))
                if start_dir != os.path.dirname(__file__):
                    break
            else:
                raise ValueError('Unable to find a start directory.')
        self.app_factory = app_factory
        self.default_pattern = pattern
        self.default_start_dir = start_dir
        self.default_verbosity = 4

    def get_options(self):
        return [
            Option('--verbosity', '-v', dest='verbosity',
                   help='The verbosity level', default=self.default_verbosity),
            Option('--pattern', '-p', dest='pattern',
                   help='Pattern to search for features',
                   default=self.default_pattern),
            Option('--start-dir', '-s', dest='start_dir',
                   help='Start directory', default=self.default_start_dir),
            #Option('--run-server', '-r', dest='run_server',
                   #help='Run a development server', default=False),
            #Option('--run-server-port', '-o', dest='server_port',
                   #help='Development server port', default=5000),
            #Option('--run-server-host', '-t', dest='server_host',
            #       help='Development server host', default='localhost')
        ]

    def get_path(self, start_dir, pattern):
        """
        Get all paths inside `start_dir` that matched `pattern`

        :param start_dir start directory to scan for features
        :param pattern pattern of the features directory
        """
        paths = []
        for dirpath, dirs, files in os.walk(os.path.abspath(start_dir)):
            for dirname in dirs:
                fullname = os.path.join(dirpath, dirname)
                if fnmatch.fnmatch(fullname, pattern):
                    paths.append(fullname)
        return paths

    def run(self, verbosity, pattern, start_dir):
        """
        Harvest all Lettuce features from the current application
        """
        paths = self.get_path(start_dir, pattern)
        results = []
        failed = False

        app_factory = self.app_factory

        @before.each_scenario
        def setup_scenario(feature):
            world.app = app_factory()
            world.client = world.app.test_client()

        @after.each_scenario
        def teardown_scenario(scenario):
            del world.client
            del world.app

        registry.call_hook('before', 'harvest', locals())
        try:
            for path in paths:
                runner = Runner(path, verbosity=verbosity)
                result = runner.run()
                results.append(result)
                if not result or result.steps != result.steps_passed:
                    failed = True
        except Exception, e:
            import traceback
            traceback.print_exc(e)
        finally:
            registry.call_hook('after', 'harvest', results)
            if failed:
                print "Failed"
