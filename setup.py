import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='visualize_logs',
    version='20161021.1',
    author='Keith J. Jones',
    author_email='keith@keithjjones.com',
    packages=['Visualize_Logs'],
    url='https://github.com/keithjjones/visualize_logs',
    license='LICENSE',
    description=('A Python library to '
                 'provide log visualization.'),
    long_description=read('README.TXT'),
    install_requires=['networkx', 'pandas', 'plotly>=1.9.0',
                      'pydotplus'],
    entry_points={
        'console_scripts': [
            'plotprocmoncsv = Visualize_Logs.__main__:plotprocmoncsv'
        ]
     }
)
