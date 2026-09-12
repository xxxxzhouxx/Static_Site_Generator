import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node1 = TextNode("This is a text node", TextType.Text)
        result1 = split_nodes_delimiter([node1], "**", TextType.Text)
        self.assertEqual (result1, [node1])
        # Plain text test

        node2 = TextNode("This is a **bold text** node", TextType.Text)
        result2 = split_nodes_delimiter([node2], "**", TextType.Bold)
        self.assertEqual(result2, [TextNode("This is a ", TextType.Text), TextNode("bold text", TextType.Bold), TextNode(" node", TextType.Text)])
        # Bold text test

        node3 = TextNode("This is a _italic text node_", TextType.Text)
        result3 = split_nodes_delimiter([node3], "_", TextType.Italic)
        self.assertEqual(result3, [TextNode("This is a ", TextType.Text), TextNode("italic text node", TextType.Italic)])
        # Italic text test

        node4 = TextNode("This is a `code` text node", TextType.Text)
        result4 = split_nodes_delimiter([node4], "`", TextType.Code)
        self.assertEqual(result4, [TextNode("This is a ", TextType.Text), TextNode("code", TextType.Code), TextNode(" text node", TextType.Text)])
        # Code text test

if __name__ == "__main__":
    unittest.main()