from md_to_blocks import md_to_blocks
import unittest

class Test_md_to_blocks(unittest.TestCase):
    def test_md_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = md_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                ],
            )

        md = """
        This is **bolded** paragraph
        with an additional sentence

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = md_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\nwith an additional sentence",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                ],
            )
