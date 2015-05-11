"""
Flask Config Override
-----
"""

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()
test_requirements = ['flask']
setup(name='config_override',
      version='0.1',
      description='Python utilities for loading config',
      url='https://github.com/MentorWebServiceTeam/flask-config-override',
      author='Josh Frankamp',
      author_email='joshua_frankamp@mentor.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      test_suite='tests',
      zip_safe=False,
      test_require=test_requirements,
      install_requires=[])