"""
Flask Config Override
-----
"""

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

test_requirements = [
    'flask==0.10.1',
    'nose==1.3.6',
    'coverage==3.7.1'
]

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
      extras_require={
          'test': test_requirements,
      },
      install_requires=[])
