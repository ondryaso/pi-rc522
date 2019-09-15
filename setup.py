#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

setup(
    name='pi-rc522',
    packages=find_packages(),
    include_package_data=True,
    version='2.3.1',
    description='Raspberry Pi Python library for SPI RFID RC522 module.',
    long_description='Raspberry Pi Python library for SPI RFID RC522 module.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    author='ondryaso',
    author_email='ondryaso@ondryaso.eu',
    url='https://github.com/kevinvalk/pi-rc522',
    license='MIT',
    install_requires=['spidev', 'RPi.GPIO'],
)
