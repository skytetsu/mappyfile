import re
from setuptools import setup

__version__,= re.findall('__version__ = "(.*)"', open('mappyfile/__init__.py').read())

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mappyfile',
      version=__version__,
      description='A pure Python MapFile parser for working with MapServer',
      long_description=readme(),
      classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Build Tools'
      ],
      package_data = {
        '': ['*.g', 'schemas/*.json']
      },
      url='http://github.com/geographika/mappyfile',
      author='Seth Girvin',
      author_email='sethg@geographika.co.uk',
      license='MIT',
      packages=['mappyfile'],
      install_requires=['lark-parser','jsonschema'],
      zip_safe=False)