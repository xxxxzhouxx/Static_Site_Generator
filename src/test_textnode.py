import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a bold text node", TextType.Bold)
        node4 = TextNode("This is a italic text node", TextType.Italic)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is some anchor text", TextType.Link, "https://www.boot.dev")
        node6 = TextNode("This is some anchor text", TextType.Link)
        self.assertNotEqual(node5, node6)

        node7 = TextNode("This is a text node", TextType.Text)
        html_node = text_node_to_html_node(node7)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node8 = TextNode("This is a bold text node", TextType.Bold)
        html_node2 = text_node_to_html_node(node8)
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is a bold text node")

        node9 = TextNode("This is a link", TextType.Link, "https://www.boot.dev")
        html_node3 = text_node_to_html_node(node9)
        self.assertEqual(html_node3.tag, "a")
        self.assertEqual(html_node3.value, "This is a link")
        self.assertEqual(html_node3.props, {"href": "https://www.boot.dev"})

if __name__ == "__main__":
    unittest.main()