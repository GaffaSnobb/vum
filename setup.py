from setuptools import setup

setup(
    name = 'vum',
    version = '1.0.0.1',    
    description = 'A simple UI with curses',
    # long_description = long_description,
    url = 'https://github.com/GaffaSnobb/vum',
    author = ['Jon Kristian Dahl',],
    author_email = 'jonkd@uio.no',
    packages = ['vum'],
    install_requires = [],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.11',
    ],
)
