from typing import Any, Dict, List, Tuple

import yaml
from markdown import Extension, Markdown
from markdown.preprocessors import Preprocessor


class FullYamlMetadataExtension(Extension):
    """Extension for parsing YAML metadata part with Python-Markdown."""

    def __init__(self, **kwargs: Any):
        self.config = {
            "yaml_loader": [
                yaml.FullLoader,
                "YAML loader to use. Default: yaml.FullLoader",
            ],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: Markdown, *args: Any, **kwargs: Any) -> None:
        md.registerExtension(self)
        md.Meta = None  # type: ignore
        md.preprocessors.register(
            FullYamlMetadataPreprocessor(md, self.getConfigs()),
            "full_yaml_metadata",
            1,
        )


class FullYamlMetadataPreprocessor(Preprocessor):
    """Preprocess markdown content with YAML metadata parsing.

    YAML block is delimited by '---' at start and '...' or '---' at end.

    """

    def __init__(self, md: Markdown, config: Dict[str, Any]):
        super().__init__(md)
        self.config = config

    def run(self, lines: List[str]) -> List[str]:
        meta_lines, lines = self.split_by_meta_and_content(lines)

        loader = self.config.get("yaml_loader", yaml.FullLoader)
        self.md.Meta = yaml.load("\n".join(meta_lines), Loader=loader)
        return lines

    def split_by_meta_and_content(
        self, lines: List[str]
    ) -> Tuple[List[str], List[str]]:
        meta_lines: List[str] = []
        if lines[0] != "---":
            return meta_lines, lines

        lines.pop(0)
        for line in lines:  # type: str
            if line in ("---", "..."):
                content_starts_at = lines.index(line) + 1
                lines = lines[content_starts_at:]
                break

            meta_lines.append(line)

        return meta_lines, lines


def makeExtension(*args: Any, **kwargs: Any) -> FullYamlMetadataExtension:
    return FullYamlMetadataExtension(*args, **kwargs)
