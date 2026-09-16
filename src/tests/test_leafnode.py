import os, sys, inspect
import unittest

current_dir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(inspect.currentframe())  # pyright: ignore[reportArgumentType]
    )
)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_img(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")
