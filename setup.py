# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

f = open('README.md')
readme = f.read().strip()

f = open('LICENSE.md')
license = f.read().strip()

setup(
    name='piapp',
    version='0.7.1',
    description='Open Metadata ',
    long_description=readme,
    author='Abstract Factory Ltd.',
    author_email='marcus@abstractfactory.com',
    url='https://github.com/abstractfactory/piapp',
    license=license,
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    zip_safe=False,
)
