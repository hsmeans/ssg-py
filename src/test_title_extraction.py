import unittest

from title_extraction import extract_title


class TestTitleExtraction(unittest.TestCase):
    def test_title_extraction(self):
        expected = "Hello"
        val = extract_title("# Hello")
        self.assertEqual(expected, val)

    def test_title_extraction_whitespace(self):
        expected = "Hello"
        val = extract_title("     #              Hello             ")
        self.assertEqual(expected, val)

    def test_title_extraction_newlines(self):
        expected = "Hello"
        val = extract_title("# Hello\n\n Other line")
        self.assertEqual(expected, val)

    def test_title_extraction_failure(self):
        with self.assertRaises(ValueError):
            extract_title("Hello")
        with self.assertRaises(ValueError):
            extract_title("## Hello")
        with self.assertRaises(ValueError):
            extract_title("# ")
        with self.assertRaises(ValueError):
            extract_title("")
        with self.assertRaises(ValueError):
            extract_title("#")
        with self.assertRaises(ValueError):
            extract_title("#Hello")
