#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0', 'feedparser', 'beautifulsoup4',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='ahps_alerts',
    version='0.1.5',
    description="Retrieve NWS AHPS alerts",
    long_description=readme + '\n\n' + history,
    author="David Hickman",
    author_email='david.hickman@twdb.texas.gov',
    url='https://github.com/DavidHickman/ahps_alerts',
    packages=find_packages(include=['ahps_alerts']),
    entry_points={
        'console_scripts': [
            'ahps-alerts=ahps_alerts.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ahps_alerts, National Weather Service, TNRIS, Texas',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
