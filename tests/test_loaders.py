import datetime
import typing

import markdown
import pytest
import yaml

SOURCE = """---
title: What is Lorem Ipsum?
category: Lorem Ipsum
date: 2020-01-01 10:00:00
num_comments: 5
...

Lorem Ipsum is simply dummy text.
"""


@pytest.mark.parametrize(
    "loader, expected_meta",
    (
        [
            # Only loads the most basic YAML. All scalars are loaded as strings.
            yaml.BaseLoader,
            {
                "title": "What is Lorem Ipsum?",
                "category": "Lorem Ipsum",
                "date": "2020-01-01 10:00:00",
                "num_comments": "5",
            },
        ],
        [
            # Loads a subset of the YAML language, safely. This is recommended
            # for loading untrusted input.
            yaml.SafeLoader,
            {
                "title": "What is Lorem Ipsum?",
                "category": "Lorem Ipsum",
                "date": datetime.datetime(2020, 1, 1, 10, 0, 0),
                "num_comments": 5,
            },
        ],
        [
            # Loads the full YAML language. Avoids arbitrary code execution,
            # but still trivially exploitable. Do not use for untrusted data
            # input.
            yaml.FullLoader,
            {
                "title": "What is Lorem Ipsum?",
                "category": "Lorem Ipsum",
                "date": datetime.datetime(2020, 1, 1, 10, 0, 0),
                "num_comments": 5,
            },
        ],
    ),
)
def test_custom_loader(
    loader: typing.Any,
    expected_meta: typing.Dict[str, typing.Any],
) -> None:
    md = markdown.Markdown(
        extensions=["full_yaml_metadata"],
        extension_configs={
            "full_yaml_metadata": {
                "yaml_loader": loader,
            }
        },
    )

    md.convert(SOURCE)
    assert md.Meta == expected_meta
