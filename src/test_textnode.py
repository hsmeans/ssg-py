import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is not a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is not a text node", TextType.LINK, "example.com")
        node2 = TextNode("This is not a text node", TextType.LINK, "example.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is not a text node", TextType.IMAGE, "example.com")
        node2 = TextNode("This is not a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        text = "This is an anchor node"
        href = "example.com"
        node = TextNode(text, TextType.LINK, href)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props, {"href": href})

    def test_img(self):
        alt = "This is alt text"
        src = "example.com"
        node = TextNode(alt, TextType.IMAGE, src)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"alt": alt, "src": src})


if __name__ == "__main__":
    unittest.main()
