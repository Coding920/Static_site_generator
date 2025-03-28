import unittest

from textnode import TextType, TextNode
from text_to_node import text_node_to_html_node


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

    # Function text to node testing
    def test_normal_transform(self):
        text_node = TextNode("normal text", TextType.Normal)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            "self.tag=None\nself.value='normal text'\nself.children=None\nself.props=None",
            html_node.__repr__()
            )
    
    def test_bold_transform(self):
        bold_node = TextNode("bold text", TextType.Bold)
        html_node = text_node_to_html_node(bold_node)
        self.assertEqual(
            "self.tag='b'\nself.value='bold text'\nself.children=None\nself.props=None",
            html_node.__repr__()
            )

    def test_italic_transform(self):
        italic_node = TextNode("italic text", TextType.Italic)
        html_node = text_node_to_html_node(italic_node)
        self.assertEqual(
            "self.tag='i'\nself.value='italic text'\nself.children=None\nself.props=None",
            html_node.__repr__()
            )

    def test_link_transform(self):
        link_node = TextNode("link text", TextType.Link, "boot.dev")
        html_node = text_node_to_html_node(link_node)
        self.assertEqual(
            "self.tag='a'\nself.value='link text'\nself.children=None\nself.props={'href': 'boot.dev'}",
            html_node.__repr__()
            )

    def test_image_transform(self):
        image_node = TextNode("alt text", TextType.Image, "boot.dev")
        html_node = text_node_to_html_node(image_node)
        self.assertEqual(
            "self.tag='img'\nself.value=''\nself.children=None\nself.props={'src': 'boot.dev', 'alt': 'alt text'}",
            html_node.__repr__()
            )



if __name__ == "__main__":
    unittest.main()
