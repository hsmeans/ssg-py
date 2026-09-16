from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
        super().__init__()

    def __eq__(self, value: object) -> bool:
        if isinstance(value, TextNode):
            return (
                self.text == value.text
                and self.text_type == value.text_type
                and self.url == value.url
            )
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text, tag, props = "", None, None
    match text_node.text_type:
        case TextType.TEXT:
            tag = None
            text = text_node.text
        case TextType.BOLD:
            tag = "b"
            text = text_node.text
        case TextType.ITALIC:
            tag = "i"
            text = text_node.text
        case TextType.CODE:
            tag = "code"
            text = text_node.text
        case TextType.LINK:
            tag = "a"
            text = text_node.text
            props = {"href": text_node.url}
        case TextType.IMAGE:
            tag = "img"
            props = {"src": text_node.url, "alt": text_node.text}
        case _:
            raise Exception()

    return LeafNode(tag, text, props)
