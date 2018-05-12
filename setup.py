#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Installation instructions and package metadata."""

from setuptools import setup


# Put the modules which need to be installed as actual scripts in here.
SCRIPTS = [
    'images_to_video',
    'video_to_images'
]

CONSOLE_SCRIPTS = ['{0} = utils.{0}:main'.format(script) for script in
                   SCRIPTS]


setup(
    name='Computer-Vision',
    version='1.0.0',
    author='Meedhunbala',
    author_email='bala_me17781@yahoo.co.in',
    # third-party packages
    install_requires=[
        'opencv-python',
    ],
    packages=['utils'],
    entry_points={'console_scripts': CONSOLE_SCRIPTS},
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Topic :: Engineering :: ComputerVision'
    ],
    description=("A toolset for CV "),
    long_description=open('README.rst').read(),
)
