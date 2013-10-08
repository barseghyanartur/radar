import os
from setuptools import setup, find_packages

try:
  readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
  readme = ''

version = '0.3'

setup(
    name = 'radar',
    version = version,
    description = ("Random date generation."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],
    keywords = 'random date, python',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    url = 'https://bitbucket.org/barseghyanartur/radar',
    license = 'GPL 2.0/LGPL 2.1',
)
