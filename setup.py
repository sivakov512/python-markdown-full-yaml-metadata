from setuptools import setup

url = 'https://github.com/cryptomaniac512/python-markdown-full-yaml-metadata'


setup(
    author='Nikita Sivakov',
    author_email='cryptomaniac.512@gmail.com',
    description='YAML metadata extension for Python-Markdown',
    install_requires=['Markdown', 'PyYAML'],
    keywords='markdown yaml meta metadata',
    license='MIT',
    long_description_markdown_filename='README.md',
    name='makrdown_full_yaml_metadata',
    py_modules=['full_yaml_metadata'],
    setup_requires=['setuptools-markdown'],
    url=url,
    version='0.0.5',
)
