import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author='Nikita Sivakov',
    author_email='sivakov512@gmail.com',
    description='YAML metadata extension for Python-Markdown',
    install_requires=['Markdown==3.0.1', 'PyYAML>=3.13'],
    keywords='markdown yaml meta metadata',
    license='MIT',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    name='markdown-full-yaml-metadata',
    py_modules=['full_yaml_metadata'],
    python_requires='>=3.4',
    setup_requires=['setuptools-markdown'],
    version='0.0.4',
    url='https://github.com/sivakov512/python-markdown-full-yaml-metadata',
)
