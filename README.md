# YAML metadata extension for [Python-Markdown](https://github.com/waylan/Python-Markdown)

[![Build Status](https://travis-ci.org/sivakov512/python-markdown-full-yaml-metadata.svg?branch=master)](https://travis-ci.org/sivakov512/python-markdown-full-yaml-metadata)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/python-markdown-full-yaml-metadata/badge.svg)](https://coveralls.io/github/sivakov512/python-markdown-full-yaml-metadata)
![Python versions](https://img.shields.io/badge/python-3.4,%203.5,%203.6-blue.svg)
[![PyPi](https://img.shields.io/pypi/v/markdown-full-yaml-metadata.svg)](https://pypi.python.org/pypi/markdown-full-yaml-metadata)

This extension adds YAML meta data handling to markdown with all YAML features.

As in the original, metadata is parsed but not used in processing.

Metadata parsed as is by PyYaml and without additional transformations, so this plugin is not compatible with original [Meta-Data extension](https://pythonhosted.org/Markdown/extensions/meta_data.html).


## Basic Usage

``` python
import markdown


text = """---
title: What is Lorem Ipsum?
categories:
	- Lorem Ipsum
	- Stupid content
...

Lorem Ipsum is simply dummy text.
"""

md = markdown.Markdown(['full_yaml_metadata'])
md.convert(text) == '<p>Lorem Ipsum is simply dummy text.</p>'
md.Meta == {'title': 'What is Lorem Ipsum?', 'categories': ['Lorem Ipsum', 'Stupid content']}
```
	
## Python versions compatibility

This plugin tested with python versions 3.4, 3.5 and 3.6.

For python 3.4 you must install [typing](https://pypi.python.org/pypi/typing)
