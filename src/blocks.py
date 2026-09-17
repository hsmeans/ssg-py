from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"

    def __init__(self, type, heading_level=1) -> None:
        super().__init__()
        self.type = type
        self.heading_level = heading_level

    def __str__(self) -> str:
        if self.type == self.HEADING:
            return f"{self.type}{self.heading_level}"
        return self.type


def markdown_to_blocks(markdown: str) -> list[str]:
    res = []
    lines = markdown.split("\n\n")
    for li in lines:
        sli = li.strip()
        if not sli:
            continue
        res.append(sli)

    return res


def block_to_block_type(block: str) -> BlockType:
    if block[0] == "#":
        count = 0
        for ch in block:
            if ch == "#" and count < 6:
                count += 1
                continue
            if ch == " ":
                type = BlockType.HEADING
                type.heading_level = count
                return type
            else:
                break
    if len(block) >= 2 and block[:2] == "> ":
        return BlockType.QUOTE
    if len(block) >= 2 and block[:2] == "- ":
        lines = block.split("\n")
        flag = True
        for li in lines:
            if len(li) >= 2 and li[:2] == "- ":
                continue
            else:
                flag = False
                break
        if flag:
            return BlockType.UNORDERED_LIST
    if len(block) >= 3 and block[:3] == "1. ":
        cur = 1
        lines = block.split("\n")
        flag = True
        for li in lines:
            if len(li) >= 3 and li[:3] == f"{cur}. ":
                cur += 1
            else:
                flag = False
                break
        if flag:
            return BlockType.ORDERED_LIST
    if len(block) >= 8 and block[:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE

    return BlockType.PARAGRAPH
