#!/usr/bin/env python

from __future__ import absolute_import
from telex import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requires = [
    'requests>=2.6.0',
]

with open('README.md') as f:
    readme = f.read()

setup(
    name='telex',
    version=__version__,
    description='Python telex client.',
    long_description=readme,
    license='MIT',
    author='Jeremy West',
    author_email='jeremy@heroku.com',
    url='https://github.com/heroku/python-telex',
    packages=['telex'],
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
