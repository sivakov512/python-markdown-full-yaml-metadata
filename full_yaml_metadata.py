import typing

import markdown
import yaml


class FullYamlMetadataExtension(markdown.Extension):
    """Extension for parsing YAML metadata part with Python-Markdown."""
    def __init__(self, **kwargs):
        self.config = {
            "yaml_loader": [
                yaml.FullLoader,
                "YAML loader to use. Default: yaml.FullLoader",
            ],
            "allow_missing_delimiters": [
                False,
                "Attempt to split by blank line if metadata delimiters were "
                "not found. Default: False",
            ],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: markdown.Markdown, *args, **kwargs):
        md.registerExtension(self)
        md.Meta = None
        md.preprocessors.register(
            FullYamlMetadataPreprocessor(md, self.getConfigs()),
            "full_yaml_metadata",
            1,
        )


class FullYamlMetadataPreprocessor(markdown.preprocessors.Preprocessor):
    """Preprocess markdown content with YAML metadata parsing.

    YAML block is delimited by '---' at start and '...' or '---' at end.

    """

    def __init__(self, md, config):
        super().__init__(md)
        self.config = config

    def run(self, lines: list) -> list:
        metadata, content_lines = self.parse_meta_delimited(lines)
        if metadata is None and self.config.get("allow_missing_delimiters"):
            metadata, content_lines = self.parse_meta_fuzzy(lines)
        self.md.Meta = metadata

        return content_lines

    def parse_meta_block(self, meta):
        loader = self.config.get("yaml_loader", yaml.FullLoader)
        return yaml.load(meta, Loader=loader)

    def parse_meta_delimited(self, lines: list) -> typing.Tuple[dict, list]:
        """
        Find and parse YAML data in text by looking for delimiters.
        """
        meta_lines = []
        if lines[0] != "---":
            # YAML metadata delimiters not found
            return None, lines

        content_lines = []
        for i, line in enumerate(lines[1:], start=1):  # type: str
            if line in ("---", "..."):
                content_starts_at = i + 1
                content_lines = lines[content_starts_at:]
                break

            meta_lines.append(line)

        metadata = self.parse_meta_block("\n".join(meta_lines))
        return metadata, content_lines

    def parse_meta_fuzzy(self, lines: list) -> typing.Tuple[dict, list]:
        """
        Find and parse YAML data in text by splitting by the first blank line.
        """

        content_starts_at = lines.index('') + 1
        meta_lines = lines[:content_starts_at]
        content_lines = lines[content_starts_at:]

        try:
            metadata = self.parse_meta_block("\n".join(meta_lines))
        except yaml.error.YAMLError:
            return None, lines

        # Prevent false-positives if the text does not begin with a
        # metadata block
        if isinstance(metadata, str):
            return None, lines

        return metadata, content_lines


def makeExtension(*args, **kwargs):
    return FullYamlMetadataExtension(*args, **kwargs)
