from html_page_helpers import extract_title
import unittest

class Test_html_helpers(unittest.TestCase):
    def test_extract_title(self):
        text = "# This is a test title"
        title = extract_title(text)
        self.assertEqual(title, "This is a test title")
