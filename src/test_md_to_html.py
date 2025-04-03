import unittest
from md_to_htmlnode import md_to_htmlnode



class test_md_to_html(unittest.TestCase):
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_paragraphs2(self):
        md = """
        this is a paragraph
        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>this is a paragraph</p></div>",
        )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
        >this is a
        >quote block
        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is a\nquote block</blockquote></div>",
        )

    def test_headingblock(self):
        md = """
        ### this is a triple heading block
        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>this is a triple heading block</h3></div>",
        )

    def test_orderedlist_block(self):
        md = """
        1. this is
        2. an ordered
        3. list block
        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>this is</li><li>an ordered</li><li>list block</li></ol></div>",
        )

    def test_unorderedlist_block(self):
        md = """
        - this is
        - an unordered
        - list block
        """
        node = md_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is</li><li>an unordered</li><li>list block</li></ul></div>",
            )

    def test_specific_bolding_issue(self):
        md = "This series, in my many years as **Archmage**, the world."
        html = md_to_htmlnode(md)
        self.assertEqual(
                html.to_html(),
            "<div><p>This series, in my many years as <b>Archmage</b>, the world.</p></div>"
            )

    def test_specific_orderedlistblock_issue(self):
        md = """
1. An elaborate pantheon of deities (the `Valar` and `Maiar`)
2. The tragic saga of the Noldor Elves
        """
        html = md_to_htmlnode(md)
        self.assertEqual(
                html.to_html(),
                "<div><ol><li>An elaborate pantheon of deities (the <code>Valar</code> and <code>Maiar</code>)</li><li>The tragic saga of the Noldor Elves</li></ol></div>"
            )


    if __name__ == "__main__":
        unittest.main()
