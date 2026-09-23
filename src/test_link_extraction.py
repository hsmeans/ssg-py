import unittest

from link_extraction import extract_markdown_images, extract_markdown_links


class TestExtractLink(unittest.TestCase):
    def test_valid(self):
        text = "This is text with a link [to site](https://www.example.com) and [to youtube](https://www.youtube.com/)"
        matches = extract_markdown_links(text)
        self.assertEqual(
            matches,
            [
                ("to site", "https://www.example.com"),
                ("to youtube", "https://www.youtube.com/"),
            ],
        )

    def test_invalid(self):
        text = "This is text without a valid link [to site]https://www.example.com) or [to youtube(https://www.youtube.com/)"
        matches = extract_markdown_links(text)
        self.assertEqual(
            matches,
            [],
        )


class TestExtractImage(unittest.TestCase):
    def test_valid(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(
            matches,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_invalid(self):
        text = "This is not text with a ![rick roll]https://i.imgur.com/aKaOqIh.gif) or [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(
            matches,
            [],
        )
