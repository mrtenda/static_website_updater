#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="static_website_updater",
    version="1",
    packages=find_packages(),

    install_requires=[
        "boto",
        "flickrapi",
        "GitPython"
    ]
)
