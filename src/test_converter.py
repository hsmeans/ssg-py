import unittest

from converter import markdown_to_html_node


class TestConverter(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(
            html,
            expected,
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"

        self.assertEqual(html, expected)

    def test_unordered_list(self):
        md = """
## List of numbers I like

- 1
- 2
- 3
- 4
- 5
"""
        expected = "<div><h2>List of numbers I like</h2><ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li></ul></div>"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_ordered_list(self):
        md = """
##### List of things I hate

1. numbered lists
2. code blocks
3. tests that don't respect the reality of html
"""
        expected = "<div><h5>List of things I hate</h5><ol><li>numbered lists</li><li>code blocks</li><li>tests that don't respect the reality of html</li></ol></div>"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)
