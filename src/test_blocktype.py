from blocktype import BlockType, block_to_block_type
from md_to_blocks import md_to_blocks
import unittest

class test_block_to_block_type(unittest.TestCase):
    def test_blocktype_heading(self):
        md = """
        ### 3 heading block
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.Heading]
            )

    def test_blocktype_quote(self):
        md = """
        >quote
        >block
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.Quote]
            )

    def test_blocktype_code(self):
        md = """
        ```
        code block
        ```
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.Code]
            )

    def test_blocktype_ul(self):
        md = """
        - unordered
        - block
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.UL]
            )

    def test_blocktype_ol(self):
        md = """
        1. ordered
        2. block
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.OL]
            )

    def test_blocktype_paragraph(self):
        md = """
        this is a paragraph
        block
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.Paragraph]
            )

    def test_blocktype_with_improper_formatting(self):
        md = """
        1. this is an improper
        2. ordered list
        BeCaUsE oF ThIs
        """
        blocks = md_to_blocks(md)
        final = []
        for block in blocks:
            final.append(block_to_block_type(block))
        self.assertEqual(
            final,
            [BlockType.Paragraph]
            )


