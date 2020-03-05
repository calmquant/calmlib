#!/usr/bin/env python

from distutils.core import setup
from pathlib import Path

setup(name='Calmlib',
      version='0.1.0',
      description='Calmlib',
      author='Petr Lavrov',
      author_email='calmquant@gmail.com',
      url='https://github.com/calmquant/calmlib',
      packages=['calmlib'],
      long_description=Path('README.md').read_text(),
      install_requires=Path('requirements.txt').read_text().split()
      )
