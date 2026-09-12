import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("span", "This is a span", {"class": "highlight"})
        self.assertEqual(node2.to_html(), '<span class="highlight">This is a span</span>')
        node3 = LeafNode("a", None, {"href": "https://www.example.com"})
        self.assertRaises(ValueError, node3.to_html)
        

if __name__ == "__main__":
    unittest.main()