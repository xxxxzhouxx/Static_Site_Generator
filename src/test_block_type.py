import unittest
from blocks import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_heading_block(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.Heading)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```python\nprint('Hello, World!')\n```"), BlockType.Code)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.Quote)

    def test_unordered_list_block(self):
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.Unordered_list)

    def test_ordered_list_block(self):
        self.assertEqual(block_to_block_type("1. Item 1"), BlockType.Ordered_list)

    def test_paragraph_block(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.Paragraph)