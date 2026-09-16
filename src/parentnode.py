from functools import reduce

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict | None = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("tag is required for parent node")
        if self.children == None:
            raise ValueError("children are required for parent node")
        return f"<{self.tag}>{reduce(lambda x, y: x + y.to_html(), self.children, "")}</{self.tag}>"
