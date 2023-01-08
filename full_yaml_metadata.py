import typing

import yaml
from markdown import Extension, Markdown
from markdown.preprocessors import Preprocessor


class FullYamlMetadataExtension(Extension):
    """Extension for parsing YAML metadata part with Python-Markdown."""

    def __init__(self, **kwargs: typing.Any):
        self.config = {
            "yaml_loader": [
                yaml.FullLoader,
                "YAML loader to use. Default: yaml.FullLoader",
            ],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: Markdown, *args: typing.Any, **kwargs: typing.Any) -> None:
        md.registerExtension(self)
        md.Meta = None  # type: ignore
        md.preprocessors.register(
            FullYamlMetadataPreprocessor(md, self.getConfigs()), "full_yaml_metadata", 1
        )


class FullYamlMetadataPreprocessor(Preprocessor):
    """Preprocess markdown content with YAML metadata parsing.

    YAML block is delimited by '---' at start and '...' or '---' at end.

    """

    def __init__(self, md: Markdown, config: typing.Dict[str, typing.Any]):
        super().__init__(md)
        self.config = config

    def run(self, lines: typing.List[str]) -> typing.List[str]:
        meta_lines, lines = self.split_by_meta_and_content(lines)

        loader = self.config.get("yaml_loader", yaml.FullLoader)
        self.md.Meta = yaml.load("\n".join(meta_lines), Loader=loader)  # type: ignore
        return lines

    @staticmethod
    def split_by_meta_and_content(
        lines: typing.List[str],
    ) -> typing.Tuple[typing.List[str], typing.List[str]]:
        meta_lines: typing.List[str] = []
        if lines[0].rstrip(" ") != "---":
            return meta_lines, lines

        lines.pop(0)
        for line in lines:  # type: str
            if line.rstrip(" ") in ("---", "..."):
                content_starts_at = lines.index(line) + 1
                lines = lines[content_starts_at:]
                break

            meta_lines.append(line)

        return meta_lines, lines


def makeExtension(*args: typing.Any, **kwargs: typing.Any) -> FullYamlMetadataExtension:
    return FullYamlMetadataExtension(*args, **kwargs)
