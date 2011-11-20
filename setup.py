"""
Flask-Lettuce
-------------

Add Lettuce support for Flask application

Links
`````

* `documentation <http://packages.python.org/Flask-Lettuce>`_
* `development version
  <http://github.com/dqminh/flask-lettuce/zipball/master#egg=Flask-Lettuce-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-Lettuce',
    version='0.1',
    url='<enter URL here>',
    license='BSD',
    author='Daniel, Dao Quang Minh (dqminh)',
    author_email='dqminh89@gmail.com',
    description='Add Lettuce support for Flask application',
    long_description=__doc__,
    py_modules=['flask_lettuce'],
    zip_safe=False,
    platforms='any',
    test_suite='test',
    install_requires=[
        'Flask',
        'Flask-Script',
        'Lettuce',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
