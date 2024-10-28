#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='roll',
    version=read('VERSION'),
    description='A command line tool which simulates rolling a die',
    long_description=read('README.md'),
    long_description_content_type='text/x-markdown',
    keywords='D&D Dice Roll CLI',
    author='David Haller',
    author_email='haller_david@icloud.com',
    license='GPLv3',
    url='https://github.com/davidhaller/roll',
    download_url = 'https://github.com/davidhaller/roll/archive/master.zip',
    packages=find_packages(),
    package_data={
        'roll': ['../VERSION']
    },
    entry_points={
        'console_scripts': [
            'roll = roll.__main__:main',
        ]
    },
    python_requires='>=3.12',
)
