from setuptools import setup

long_description = (
    'This extenstions allow to use all YAML features in Markdown metadata part'
)
url = 'https://github.com/cryptomaniac512/python-markdown-full-yaml-metadata'


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    author='Nikita Sivakov',
    author_email='cryptomaniac.512@gmail.com',
    description='YAML metadata extension for Python-Markdown',
    install_requires=['Markdown', 'PyYAML'],
    keywords='markdown yaml meta metadata',
    license='MIT',
    long_description=readme(),
    name='makrdown_full_yaml_metadata',
    py_modules=['full_yaml_metadata'],
    url=url,
    version='0.0.3',
)
