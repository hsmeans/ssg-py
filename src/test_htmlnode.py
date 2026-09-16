import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_empty(self):
        node = str(HTMLNode())
        node2 = str(HTMLNode())
        self.assertEqual(node, node2)

    def test_eq(self):
        node = str(HTMLNode("p", "qwerty", [], {}))
        node2 = str(HTMLNode("p", "qwerty", [], {}))
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = str(HTMLNode("p", "qwerty", [], {}))
        node2 = str(HTMLNode("h", "qwerty", [], {}))
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
