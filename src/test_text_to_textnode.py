from text_to_textnode import text_to_textnodes
from textnode import TextType, TextNode
from unittest import TestCase

class test_text_to_textnode(TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
                nodes,
                [
                    TextNode("This is ", TextType.Normal),
                    TextNode("text", TextType.Bold),
                    TextNode(" with an ", TextType.Normal),
                    TextNode("italic", TextType.Italic),
                    TextNode(" word and a ", TextType.Normal),
                    TextNode("code block", TextType.Code),
                    TextNode(" and an ", TextType.Normal),
                    TextNode("obi wan image", TextType.Image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.Normal),
                    TextNode("link", TextType.Link, "https://boot.dev"),
                    ]
            )

        text = "This is **text** with an _italic_ word and a `code block` and a [link2](https://boot.dev2) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
                nodes,
                [
                    TextNode("This is ", TextType.Normal),
                    TextNode("text", TextType.Bold),
                    TextNode(" with an ", TextType.Normal),
                    TextNode("italic", TextType.Italic),
                    TextNode(" word and a ", TextType.Normal),
                    TextNode("code block", TextType.Code),
                    TextNode(" and a ", TextType.Normal),
                    TextNode("link2", TextType.Link, "https://boot.dev2"),
                    TextNode(" and an ", TextType.Normal),
                    TextNode("obi wan image", TextType.Image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.Normal),
                    TextNode("link", TextType.Link, "https://boot.dev"),
                    ]
                )
