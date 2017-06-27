#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0.1'

required = open('requirements.txt').read().split('\n')

setup(
    name='pim',
    version=version,
    description='simple cli for managing and publishing python packages',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/freeman-lab/pim',
    packages=find_packages(),
    include_package_data=True,
    entry_points = {"console_scripts": ['pim = pim.cli:cli']},
    install_requires=required,
    long_description='See https://github.com/freeman-lab/pim'
)
