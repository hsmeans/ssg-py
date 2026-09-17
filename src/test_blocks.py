import unittest
from blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        blocks = [
            "This is paragraph",
            "- This is a list\n- with items",
            "- This is not\n a list\n-sorry",
            "```\nThis is a code block\n```",
            "> This is a quote",
            "1. This\n2. is\n3. a\n4. numbered\n5. list.",
            "1. This\n2. is\n3. an\n4.accident.",
            "# h1",
            "## h2",
            "### h3",
            "#### h4",
            "##### h5",
            "###### h6",
            "####### paragraph",
            "###paragraph",
        ]
        block_types = list(map(block_to_block_type, blocks))
        self.assertEqual(
            block_types,
            [
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )


if __name__ == "__main__":
    unittest.main()
