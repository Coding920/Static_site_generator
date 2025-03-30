from unittest import TestCase
from split_node import split_nodes_delimiter, extract_md_images, extract_md_links, split_nodes_images, split_nodes_links
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

    def test_split_with_code_at_start_or_end(self):
        node = TextNode(text="`code block` at the beginning", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "`", TextType.Code)
        self.assertEqual(
                nodes,
        [TextNode(text="code block", text_type=TextType.Code), TextNode(text=" at the beginning", text_type=TextType.Normal)]
          )

        node = TextNode(text="at the end `code block`", text_type=TextType.Normal)
        nodes = split_nodes_delimiter([node], "`", TextType.Code)
        self.assertEqual(
                nodes,
        [TextNode(text="at the end ", text_type=TextType.Normal), TextNode(text="code block", text_type=TextType.Code)]
          )

        #Identify special nodes with space

    # Test Extract Markdown Image func
    def test_extract_md_images(self):
        text = "![alt text](url text) ![second alt text](second url text)"
        image_info = extract_md_images(text)
        self.assertEqual(
                image_info,
            [('alt text', 'url text'), ('second alt text', 'second url text')]
               )

        text = "![alt text](url text) [second alt text](second url text)"
        image_info = extract_md_images(text)
        self.assertEqual(
                image_info,
            [('alt text', 'url text')]
               )

        text = "![alt text](url text) !![second alt text](second url text)"
        image_info = extract_md_images(text)
        self.assertEqual(
                image_info,
            [('alt text', 'url text'), ('second alt text', 'second url text')]
               )

        text = "![alt text](url text) !![second alt text](second url text)"
        image_info = extract_md_images(text)
        self.assertEqual(
                image_info,
            [('alt text', 'url text'), ('second alt text', 'second url text')]
               )

        text = "[alt text](url text) !second alt text](second url text)"
        image_info = extract_md_images(text)
        self.assertEqual(
                image_info,
                []
               )

    # Test Extract Markdown Link func
    def test_extract_md_links(self):
        text = "[anchor text](url text) [second anchor text](second url text)"
        link_info = extract_md_links(text)
        self.assertEqual(
                link_info,
            [('anchor text', 'url text'), ('second anchor text', 'second url text')]
               )

        text = "[anchor text](url text) (second anchor text](second url text)"
        link_info = extract_md_links(text)
        self.assertEqual(
                link_info,
            [('anchor text', 'url text')]
               )

        text = "![anchor text](url text) !![second anchor text](second url text)"
        link_info = extract_md_links(text)
        self.assertEqual(
                link_info,
            [('anchor text', 'url text'), ('second anchor text', 'second url text')]
               )

    # Test Split nodes images
    def test_split_nodes_images(self):
        node = TextNode(text="This is an image link ![alt text](url) in the middle", text_type=TextType.Normal)
        new_nodes = split_nodes_images([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="This is an image link ", text_type=TextType.Normal), TextNode(text="alt text", text_type=TextType.Image, url="url"),\
                    TextNode(text=" in the middle", text_type=TextType.Normal)]
            )

        node = TextNode(text="This is an image link at the end ![alt text](url)", text_type=TextType.Normal)
        new_nodes = split_nodes_images([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="This is an image link at the end ", text_type=TextType.Normal), TextNode(text="alt text", text_type=TextType.Image, url="url")]
            )

        node = TextNode(text="![alt text](url) this is an image link at the beginning", text_type=TextType.Normal)
        new_nodes = split_nodes_images([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="alt text", text_type=TextType.Image, url="url"), TextNode(text=" this is an image link at the beginning", text_type=TextType.Normal)]
            )

        node = TextNode(text=" ![alt text](url) this is an image link at the beginning", text_type=TextType.Normal)
        new_nodes = split_nodes_images([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="alt text", text_type=TextType.Image, url="url"), TextNode(text=" this is an image link at the beginning", text_type=TextType.Normal)]
            )

        node = TextNode(text="![alt text](url) this is an image link at the beginning ", text_type=TextType.Normal)
        new_nodes = split_nodes_images([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="alt text", text_type=TextType.Image, url="url"), TextNode(text=" this is an image link at the beginning ", text_type=TextType.Normal)]
            )

    # Test Split nodes images
    def test_split_nodes_links(self):
        node = TextNode(text="This is an image link [alt text](url) in the middle", text_type=TextType.Normal)
        new_nodes = split_nodes_links([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="This is an image link ", text_type=TextType.Normal), TextNode(text="alt text", text_type=TextType.Link, url="url"),\
                    TextNode(text=" in the middle", text_type=TextType.Normal)]
            )

        node = TextNode(text="This is an image link at the end [alt text](url)", text_type=TextType.Normal)
        new_nodes = split_nodes_links([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="This is an image link at the end ", text_type=TextType.Normal), TextNode(text="alt text", text_type=TextType.Link, url="url")]
            )

        node = TextNode(text="[alt text](url) this is an image link at the beginning", text_type=TextType.Normal)
        new_nodes = split_nodes_links([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="alt text", text_type=TextType.Link, url="url"), TextNode(text=" this is an image link at the beginning", text_type=TextType.Normal)]
            )

        node = TextNode(text=" [alt text](url) this is an image link at the beginning", text_type=TextType.Normal)
        new_nodes = split_nodes_links([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="alt text", text_type=TextType.Link, url="url"), TextNode(text=" this is an image link at the beginning", text_type=TextType.Normal)]
            )

        node = TextNode(text="[alt text](url) this is an image link at the beginning ", text_type=TextType.Normal)
        new_nodes = split_nodes_links([node])
        self.assertEqual(
                new_nodes,
            [TextNode(text="alt text", text_type=TextType.Link, url="url"), TextNode(text=" this is an image link at the beginning ", text_type=TextType.Normal)]
            )

