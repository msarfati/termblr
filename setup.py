# -*- coding: utf-8 -*-

from setuptools import setup
import os

version = '0.1'


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


setup(version=version,
    name='Termblr',
    description="",
    author='Michael Sarfati, Katie Schaffer',
    author_email="michael.sarfati@utoronto.ca, k8e@",
    packages=[
        "Termblr",
        "Termblr.tests",
        "Termblr.models",
        "Termblr.utils",
        "Termblr.views",
    ],
    scripts=[
        "bin/manage.py",
    ],
    long_description="""""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    install_requires=read('requirements.txt'),

    zip_safe=False,
)
