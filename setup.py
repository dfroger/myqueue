from setuptools import setup
from myqueue import __version__

setup(
    name = 'myqueue',
    version = __version__,
    url = 'https://github.com/dfroger/myqueue',
    description = 'A queue implemented with 2 stacks, for demo purpose',
    license = 'GPL2',
    author = 'David Froger',
    author_email = 'david.froger@mailoo.org',
    packages = ['myqueue',],
)
