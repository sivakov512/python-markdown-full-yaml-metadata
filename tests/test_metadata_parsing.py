import typing

import markdown
import pytest


@pytest.mark.parametrize(
    "source, expected_meta, expected_body",
    [
        (
            """---
title: What is Lorem Ipsum?
category: Lorem Ipsum
...

Lorem Ipsum is simply dummy text.
""",
            {"title": "What is Lorem Ipsum?", "category": "Lorem Ipsum"},
            "<p>Lorem Ipsum is simply dummy text.</p>",
        ),
        (
            """---
TITLE: Where does it come from?
Author: Sivakov Nikita
---

Contrary to popular belief, Lorem Ipsum is...
""",
            {"TITLE": "Where does it come from?", "Author": "Sivakov Nikita"},
            "<p>Contrary to popular belief, Lorem Ipsum is...</p>",
        ),
    ],
)
def test_plain_metadata(
    source: str, expected_meta: typing.Dict[str, str], expected_body: str
) -> None:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta  # type: ignore


@pytest.mark.parametrize(
    "source, expected_meta, expected_body",
    (
        [
            """---
title: What is Lorem Ipsum?
categories:
    - Lorem Ipsum
    - Stupid posts
...

Lorem Ipsum is simply dummy text.
""",
            {
                "title": "What is Lorem Ipsum?",
                "categories": ["Lorem Ipsum", "Stupid posts"],
            },
            "<p>Lorem Ipsum is simply dummy text.</p>",
        ],
        [
            """---
TITLE: Where does it come from?
Authors:
    - Sivakov Nikita
    - Another Guy
---

Contrary to popular belief, Lorem Ipsum is...
""",
            {
                "TITLE": "Where does it come from?",
                "Authors": ["Sivakov Nikita", "Another Guy"],
            },
            "<p>Contrary to popular belief, Lorem Ipsum is...</p>",
        ],
    ),
)
def test_metadata_with_lists(
    source: str, expected_meta: typing.Dict[str, str], expected_body: str
) -> None:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta  # type: ignore


@pytest.mark.parametrize(
    "source, expected_meta, expected_body",
    (
        [
            """---
title: What is Lorem Ipsum?
categories:
    first: Lorem Ipsum
    second: Stupid posts
...

Lorem Ipsum is simply dummy text.
""",
            {
                "title": "What is Lorem Ipsum?",
                "categories": {
                    "first": "Lorem Ipsum",
                    "second": "Stupid posts",
                },
            },
            "<p>Lorem Ipsum is simply dummy text.</p>",
        ],
        [
            """---
TITLE: Where does it come from?
Authors:
    first: CryptoManiac
    second: Another Guy
---

Contrary to popular belief, Lorem Ipsum is...
""",
            {
                "TITLE": "Where does it come from?",
                "Authors": {"first": "CryptoManiac", "second": "Another Guy"},
            },
            "<p>Contrary to popular belief, Lorem Ipsum is...</p>",
        ],
    ),
)
def test_metadata_with_dicts(
    source: str,
    expected_meta: typing.Dict[str, typing.Union[str, typing.Dict[str, str]]],
    expected_body: str,
) -> None:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta  # type: ignore


@pytest.mark.parametrize(
    "source, expected_body",
    (
        [
            "Lorem Ipsum is simply dummy text.",
            "<p>Lorem Ipsum is simply dummy text.</p>",
        ],
        [
            "Contrary to popular belief, Lorem Ipsum is...",
            "<p>Contrary to popular belief, Lorem Ipsum is...</p>",
        ],
    ),
)
def test_without_metadata(source: str, expected_body: str) -> None:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])

    assert md.convert(source) == expected_body
    assert md.Meta is None  # type: ignore


@pytest.mark.parametrize(
    "source, expected_meta, expected_body",
    (
        [
            "---\n"
            "title: What is Lorem Ipsum?\n"
            "---        \n"
            "Lorem Ipsum is simply dummy text.\n",
            {"title": "What is Lorem Ipsum?"},
            "<p>Lorem Ipsum is simply dummy text.</p>",
        ],
        [
            "---     \n"
            "title: What is Lorem Ipsum?\n"
            "---\n"
            "Lorem Ipsum is simply dummy text.\n",
            {"title": "What is Lorem Ipsum?"},
            "<p>Lorem Ipsum is simply dummy text.</p>",
        ],
    ),
)
def test_should_support_space_after_metadata_delimiter(
    source: str, expected_meta: typing.Dict[str, str], expected_body: str
) -> None:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])

    assert md.convert(source) == expected_body
    assert md.Meta == expected_meta  # type: ignore


def test_meta_is_acceccable_before_parsing() -> None:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])

    assert md.Meta is None  # type: ignore
