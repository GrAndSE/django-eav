#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-eav',
    version='0.1.0-alpha',
    description='A simple EAV (Entity/Attribute/Value) library for django',
    author='Andrey Grygoryev',
    author_email='undeadgrandse@gmail.com',
    url='https://github.com/GrAndSE/django-eav',
    long_description=open('README', 'r').read(),
    packages=['eav', 'eav.attribute', 'eav.model', 'eav.model.attribute'],
    package_data={},
    zip_safe=False,
    requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
