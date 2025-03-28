from unittest import TestCase
from split_node import split_nodes_delimiter
from textnode import TextNode, TextType

class split_node_test(TestCase):
    def test_split_node(self):
        node = TextNode(text="This is a `code block` inside a normal block", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "`", TextType.Code)
        self.assertEqual(
                f"{nodes}", 
        "[TextNode(This is a , normal, None), TextNode(code block, code, None), TextNode( inside a normal block, normal, None)]"
        )
        node = TextNode(text="This is a _italic block_ inside a normal block", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "_", TextType.Italic)
        self.assertEqual(
                f"{nodes}", 
        "[TextNode(This is a , normal, None), TextNode(italic block, italic, None), TextNode( inside a normal block, normal, None)]"
        )
        node = TextNode(text="This is a **bold block** inside a normal block", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertEqual(
                f"{nodes}", 
        "[TextNode(This is a , normal, None), TextNode(bold block, bold, None), TextNode( inside a normal block, normal, None)]"
        )
        node = TextNode(text="This is a **bold block** inside a normal block", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertEqual(
                f"{nodes}", 
        "[TextNode(This is a , normal, None), TextNode(bold block, bold, None), TextNode( inside a normal block, normal, None)]"
        )

    def test_split_no_delimiter_found(self):
        node = TextNode(text="This is a `code block` inside a normal block", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertEqual(
                f"{nodes}", 
        "[TextNode(This is a `code block` inside a normal block, normal, None)]"
        )
        node = TextNode(text="This is a normal block of text", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertEqual(
                f"{nodes}", 
        "[TextNode(This is a normal block of text, normal, None)]"
        )
        
