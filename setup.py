#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
pip package definition
"""

from __future__ import absolute_import, print_function

import io
import re
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup

# parse requirements.txt (packages and github links)
links = []
with open("requirements.txt") as reqs_file:
    requires = reqs_file.readlines()


# read the version and info file
def read(*names, **kwargs):
    """ Read file info in correct encoding. """
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup_kwargs = {}
try:
    verstrline = read('brendapy/_version.py')
    mo = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", verstrline, re.M)
    if mo:
        verstr = mo.group(1)
        setup_kwargs['version'] = verstr
    else:
        raise RuntimeError("Unable to find version string")
except Exception as e:
    print('Could not read version: {}'.format(e))

# description from markdown
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.rst').read()
setup_kwargs['long_description'] = long_description

setup(
    name='brendapy',
    description='Parsing BRENDA information',
    url='https://github.com/matthiaskoenig/brendapy',
    author='Matthias König',
    author_email='konigmatt@googlemail.com',
    license='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    keywords='BRENDA',
    packages=find_packages(),
    package_data={
      '': [
          '../requirements.txt',
          'resources/README.txt',
          'resources/README.rst',
          'resources/brenda_download_2019-07-2019.txt',
          ],
    },
    include_package_data=True,
    zip_safe=False,
    # List run-time dependencies here.  These will be installed by pip when
    install_requires=requires,
    dependency_links=links,
    extras_require={},
    **setup_kwargs)
