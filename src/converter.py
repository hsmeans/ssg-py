from typing import Sequence

from blocks import BlockType, block_to_block_type, markdown_to_blocks
from delimiter import text_to_textnodes
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import text_node_to_html_node


def text_to_code_node(block: str) -> HTMLNode:
    return ParentNode("pre", [LeafNode("code", block[4:-3])])


def text_to_list_items(block: str, block_type: BlockType) -> list[HTMLNode]:
    if block_type != BlockType.UNORDERED_LIST and block_type != BlockType.ORDERED_LIST:
        raise ValueError("text_to_list_items only takes list blocks")
    lines = block.split("\n")
    start = 2 if block_type == BlockType.UNORDERED_LIST else 3
    items = []
    for li in lines:
        text_nodes = text_to_textnodes(li[start:].strip())
        items.append(ParentNode("li", list(map(text_node_to_html_node, text_nodes))))

    return items


def get_heading_level(block: str):
    return len(block.split("#")) - 1


def text_to_children(
    block: str, block_type: BlockType, heading_level: int = 0
) -> list[HTMLNode]:
    if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
        return text_to_list_items(block, block_type)

    clean_text = block
    if block_type == BlockType.HEADING:
        clean_text = block[heading_level:]

    if block_type == BlockType.QUOTE:
        clean_text = block[2:]

    children = []

    clean_text = " ".join(clean_text.split("\n")).strip()

    text_nodes = text_to_textnodes(clean_text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


def markdown_to_html_node(markdown: str, parent_tag="div") -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = str(block_type)
        heading_level = 0
        if block_type == BlockType.HEADING:
            heading_level = get_heading_level(block)
            tag = f"h{heading_level}"
        node = None
        if block_type == BlockType.CODE:
            node = text_to_code_node(block)
        else:
            node = ParentNode(tag, text_to_children(block, block_type, heading_level))
        nodes.append(node)

    return ParentNode(parent_tag, nodes)
