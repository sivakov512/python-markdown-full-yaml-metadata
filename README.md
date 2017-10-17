# YAML Meta Data Extension for [Python-Markdown](https://github.com/waylan/Python-Markdown)

[![Build Status](https://travis-ci.org/cryptomaniac512/python-markdown-full-yaml-metadata.svg?branch=master)](https://travis-ci.org/cryptomaniac512/python-markdown-full-yaml-metadata)
[![Coverage Status](https://coveralls.io/repos/github/cryptomaniac512/python-markdown-full-yaml-metadata/badge.svg)](https://coveralls.io/github/cryptomaniac512/python-markdown-full-yaml-metadata)

This extension adds YAML meta data handling to markdown with all YAML features.

As in the original, meta data is parsed but not used in processing.


## Basic Usage

    >>> import markdown
    >>> text = """---
    ... Title: What is Lorem Ipsum?
    ... Categories:
		- Lorem Ipsum
		- Stupid content
    ... ...
    ...
    ... Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    ... """
    >>> md = markdown.Markdown(['full_yaml_metadata'])
    >>> print(md.convert(text))
    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
    >>> print(md.Meta)
    {'title': 'What is Lorem Ipsum?', 'category': ['Lorem Ipsum', 'Stupid content']}
