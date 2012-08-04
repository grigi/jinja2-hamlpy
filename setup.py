import os
from setuptools import setup, find_packages

# This is to disable the 'black magic' surrounding versioned repositories... Terrible!
from setuptools.command import sdist
del sdist.finders[:]

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='jinja2-hamlpy',
    version = '0.1',
    description='HamlPy extension for Jinja2',
    long_description=read('README.rst'),
    author='Nickolas Grigoriadis',
    author_email='nagrigoriadis@gmail.com',
    url='http://github.com/grigi/jinja2-hamlpy',
    keywords='jinja jinja2 templates haml hamlpy',
    platforms='any',
    zip_safe=False,
    license='BSD',

    # Dependencies
    install_requires = [
        'Jinja2 >= 2.6',
        'hamlpy >= 0.80',
        'Pygments >= 1.5'
    ],

    # Packages
    py_modules=['jinja2_hamlpy'],

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "Intended Audience :: System Administrators",
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)

