# YAML metadata extension for [Python-Markdown](https://github.com/waylan/Python-Markdown)

[![Build Status](https://travis-ci.org/sivakov512/python-markdown-full-yaml-metadata.svg?branch=master)](https://travis-ci.org/sivakov512/python-markdown-full-yaml-metadata)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/python-markdown-full-yaml-metadata/badge.svg)](https://coveralls.io/github/sivakov512/python-markdown-full-yaml-metadata)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python versions](https://img.shields.io/pypi/pyversions/markdown-full-yaml-metadata.svg)](https://pypi.python.org/pypi/markdown-full-yaml-metadata)
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

md = markdown.Markdown(extensions=['full_yaml_metadata']})
md.convert(text) == '<p>Lorem Ipsum is simply dummy text.</p>'
md.Meta == {'title': 'What is Lorem Ipsum?', 'categories': ['Lorem Ipsum', 'Stupid content']}
```

### Specify a custom YAML loader

By default the full YAML loader is used for parsing, which is insecure when
used with untrusted user data. In such cases, you may want to specify a
different loader such as [`yaml.SafeLoader`](https://msg.pyyaml.org/load) using
the `extension_configs` keyword argument:

```python
import markdown
import yaml

md = markdown.Markdown(extensions=['full_yaml_metadata']}, extension_configs={
        "full_yaml_metadata": {
            "yaml_loader": yaml.SafeLoader,
        },
    },
)
```


## Development and contribution

* install project dependencies
```bash
python setup.py develop
```

* install linting, formatting and testing tools
```bash
pip install -r requirements.txt
```

* run tests
```bash
pytest
```

* run linters
```bash
flake8
mypy ./
black --check ./
```

* feel free to contribute!
