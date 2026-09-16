import os, sys, inspect

current_dir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(inspect.currentframe())  # pyright: ignore[reportArgumentType]
    )
)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from delimiter import split_nodes_delimiter


class TestDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_code_err(self):
        with self.assertRaises(ValueError):
            node = TextNode(
                "The ` code` block` delimiter` doesn't ma`ke sense", TextType.TEXT
            )
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
