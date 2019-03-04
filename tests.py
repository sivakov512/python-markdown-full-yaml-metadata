import markdown
import pytest


@pytest.mark.parametrize('source, expected_meta, expected_body', [
    ("""---
title: What is Lorem Ipsum?
category: Lorem Ipsum
...

Lorem Ipsum is simply dummy text.
""",
     {'title': 'What is Lorem Ipsum?', 'category': 'Lorem Ipsum'},
     '<p>Lorem Ipsum is simply dummy text.</p>'),
    ("""---
TITLE: Where does it come from?
Author: CryptoManiac
---

Contrary to popular belief, Lorem Ipsum is not simply random text.
""",
     {'TITLE': 'Where does it come from?', 'Author': 'CryptoManiac'},
     '<p>Contrary to popular belief, Lorem Ipsum is not simply random text.</p>'),  # noqa
])
def test_plain_metadata(source, expected_meta, expected_body):
    md = markdown.Markdown(extensions=['full_yaml_metadata'])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta


@pytest.mark.parametrize('source, expected_meta, expected_body', [
    ("""---
title: What is Lorem Ipsum?
categories:
    - Lorem Ipsum
    - Stupid posts
...

Lorem Ipsum is simply dummy text.
""",
     {'title': 'What is Lorem Ipsum?', 'categories': [
         'Lorem Ipsum', 'Stupid posts']},
     '<p>Lorem Ipsum is simply dummy text.</p>'),
    ("""---
TITLE: Where does it come from?
Authors:
    - CryptoManiac
    - Another Guy
---

Contrary to popular belief, Lorem Ipsum is not simply random text.
""",
     {'TITLE': 'Where does it come from?', 'Authors': [
         'CryptoManiac', 'Another Guy']},
     '<p>Contrary to popular belief, Lorem Ipsum is not simply random text.</p>'),  # noqa
])
def test_metadata_with_lists(source, expected_meta, expected_body):
    md = markdown.Markdown(extensions=['full_yaml_metadata'])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta


@pytest.mark.parametrize('source, expected_meta, expected_body', [
    ("""---
title: What is Lorem Ipsum?
categories:
    first: Lorem Ipsum
    second: Stupid posts
...

Lorem Ipsum is simply dummy text.
""",
     {'title': 'What is Lorem Ipsum?', 'categories': {
         'first': 'Lorem Ipsum', 'second': 'Stupid posts'}},
     '<p>Lorem Ipsum is simply dummy text.</p>'),
    ("""---
TITLE: Where does it come from?
Authors:
    first: CryptoManiac
    second: Another Guy
---

Contrary to popular belief, Lorem Ipsum is not simply random text.
""",
     {'TITLE': 'Where does it come from?', 'Authors': {
         'first': 'CryptoManiac', 'second': 'Another Guy'}},
     '<p>Contrary to popular belief, Lorem Ipsum is not simply random text.</p>'),  # noqa
])
def test_metadata_with_dicts(source, expected_meta, expected_body):
    md = markdown.Markdown(extensions=['full_yaml_metadata'])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta


@pytest.mark.parametrize('source, expected_body', [
    ('Lorem Ipsum is simply dummy text.',
     '<p>Lorem Ipsum is simply dummy text.</p>'),
    ('Contrary to popular belief, Lorem Ipsum is not simply random text.',
     '<p>Contrary to popular belief, Lorem Ipsum is not simply random text.</p>'),  # noqa
])
def test_without_metadata(source, expected_body):
    md = markdown.Markdown(extensions=['full_yaml_metadata'])

    assert md.convert(source) == expected_body
    assert md.Meta is None


def test_meta_is_acceccable_before_parsing():
    md = markdown.Markdown(extensions=['full_yaml_metadata'])

    assert md.Meta is None
