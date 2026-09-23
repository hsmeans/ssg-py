import unittest
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

    def test_leaf_to_html_link(self):
        expected = '<a href="https://www.example.com">Click me!</a>'
        html = LeafNode("a", "Click me!", {"href": "https://www.example.com"}).to_html()
        self.assertEqual(expected, html)

    def test_leaf_to_html_image(self):
        expected = '<img src="https://www.example.com" alt="example image"></img>'
        html = LeafNode(
            "img",
            "",
            {"src": "https://www.example.com", "alt": "example image"},
        ).to_html()
        self.assertEqual(expected, html)
