from setuptools import setup

url = 'https://github.com/cryptomaniac512/python-markdown-full-yaml-metadata'


setup(
    author='Nikita Sivakov',
    author_email='cryptomaniac.512@gmail.com',
    description='YAML metadata extension for Python-Markdown',
    install_requires=['Markdown', 'PyYAML==3.13'],
    keywords='markdown yaml meta metadata',
    license='MIT',
    long_description_markdown_filename='README.md',
    name='markdown-full-yaml-metadata',
    py_modules=['full_yaml_metadata'],
    python_requires='>=3.4',
    setup_requires=['setuptools-markdown'],
    url=url,
    version='0.0.3',
)
