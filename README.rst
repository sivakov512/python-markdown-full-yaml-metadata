YAML metadata extension for `Python-Markdown <https://github.com/waylan/Python-Markdown>`__
===========================================================================================

|Build Status| |Coverage Status| |Python versions| |PyPi|

This extension adds YAML meta data handling to markdown with all YAML
features.

As in the original, metadata is parsed but not used in processing.

Metadata parsed as is by PyYaml and without additional transformations,
so this plugin is not compatible with original `Meta-Data
extension <https://pythonhosted.org/Markdown/extensions/meta_data.html>`__.

Basic Usage
-----------

.. code:: python

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

Python versions compatibility
-----------------------------

This plugin tested with python versions 3.4, 3.5 and 3.6.

For python 3.4 you must install
`typing <https://pypi.python.org/pypi/typing>`__

.. |Build Status| image:: https://travis-ci.org/cryptomaniac512/python-markdown-full-yaml-metadata.svg?branch=master
   :target: https://travis-ci.org/cryptomaniac512/python-markdown-full-yaml-metadata
.. |Coverage Status| image:: https://coveralls.io/repos/github/cryptomaniac512/python-markdown-full-yaml-metadata/badge.svg
   :target: https://coveralls.io/github/cryptomaniac512/python-markdown-full-yaml-metadata
.. |Python versions| image:: https://img.shields.io/badge/python-3.4,%203.5,%203.6-blue.svg
.. |PyPi| image:: https://img.shields.io/badge/PyPi-0.0.4-yellow.svg
   :target: https://pypi.python.org/pypi/makrdown_full_yaml_metadata
