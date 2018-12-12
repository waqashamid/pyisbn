from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name = 'pyisbn',
    version = '0.0.1',
    description = 'Everything related to ISBNs',
    long_description=long_description,
    author = 'waqas',
    author_email = 'waqashamid722@gmail.com',
    url = 'https://github.com/waqashamid/pyisbn',
    license = 'Apache 2.0',
    packages = ['pyisbn.validate'],
)