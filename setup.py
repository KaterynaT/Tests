"""
Software Requirements
---------------------

- Python 2.7.x

"""
from setuptools import setup, find_packages
import subprocess

p = subprocess.Popen(["git", "describe", "--always", "--tag"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, errors = p.communicate()

if not errors:
    __version__ = output.strip()
else:
    __version__ = '0.0.0'

TESTS_REQUIRE = [
    'coverage >= 4.0.2',
    'flake8 >= 2.5.0',
    'nose >= 1.3.7',
    'mock >= 1.0.0',
]

INSTALL_REQUIRES = [
    'requests==2.7.0'
]

DEPENDENCY_LINKS = [
]

setup(
    name='progs',
    version=__version__,
    url='https://github.com/KaterynaT/Tests',
    author='Progs',
    author_email='support@katerina.com',
    description='Katerina progs',
    long_description=__doc__,
    test_suite='tests',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.json']},
    tests_require=TESTS_REQUIRE,
    install_requires=INSTALL_REQUIRES,
    dependency_links=DEPENDENCY_LINKS,
    scripts=[]
)
