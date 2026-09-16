import re

from link_extraction import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        val = node.text
        spl = val.split(delimiter)
        if len(spl) == 1:
            new_nodes.append(node)
            continue
        elif len(spl) % 2 == 0:
            raise ValueError(f"missing a closing {delimiter} in {node}")

        for i, section in enumerate(spl):
            if i == 0 and section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        val = node.text
        matches = extract_markdown_images(val)
        if not matches:
            new_nodes.append(node)
            continue
        for alt, src in matches:
            pre, val = val.split(f"![{alt}]({src})")
            if pre:
                new_nodes.append(TextNode(pre, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, src))
        if val:
            new_nodes.append(TextNode(val, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        val = node.text
        matches = extract_markdown_links(val)
        if not matches:
            new_nodes.append(node)
            continue
        for link_text, href in matches:
            pre, val = val.split(f"[{link_text}]({href})")
            if pre:
                new_nodes.append(TextNode(pre, TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, href))
        if val:
            new_nodes.append(TextNode(val, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    res = [TextNode(text, TextType.TEXT)]
    res = split_nodes_delimiter(res, "**", TextType.BOLD)
    res = split_nodes_delimiter(res, "_", TextType.ITALIC)
    res = split_nodes_delimiter(res, "`", TextType.CODE)
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    return res
