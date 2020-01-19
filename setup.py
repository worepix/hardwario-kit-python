from setuptools import setup, find_packages


NAME = 'hio'
DESCRIPTION = 'Hardwario Kit Python'
URL = 'https://github.com/pypcgc/cli-tool'
EMAIL = 'radim.kozak@hardwario.com'
AUTHOR = 'worepix'
VERSION = '0.0.1'
LICENSE = 'MIT'
CLASSIFIERS = [
        'Programming Language :: Python'
    ]


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
)
