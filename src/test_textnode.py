import unittest

from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold, "Https://example.com")
        self.assertNotEqual(node, node2)

    def test_texttype_not_eq(self):
        node = TextNode("This is a text node", TextType.Normal)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a test node", TextType.Bold) # Test
        node2 = TextNode("This is a text node", TextType.Bold) # Text
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
