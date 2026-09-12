import unittest
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node1 = ParentNode("div", [LeafNode("p", "Hello, world!")]) #parent node (tag) with a child leaf node (tag + value)
        self.assertEqual(node1.to_html(), "<div><p>Hello, world!</p></div>")

        node2 = ParentNode("div", [LeafNode("span", "This is a span", {"class": "highlight"})]) #parent node (tag) with a child leaf node (tag + value +props)
        self.assertEqual(node2.to_html(), '<div><span class="highlight">This is a span</span></div>')

        node3 = ParentNode("div", [LeafNode("a", None, {"href": "https://www.example.com"})]) #parent node (tag) with a child leaf node (tag + props) but no value
        self.assertRaises(ValueError, node3.to_html)

        node4 = ParentNode("div", [ParentNode("span", [ParentNode("p", [LeafNode("b", "This is a child of grandchild and a leaf node")], {"class": "highlight"})])]) #parent node (tag) with nested children (tag + value + props)
        self.assertEqual(node4.to_html(), '<div><span><p class="highlight"><b>This is a child of grandchild and a leaf node</b></p></span></div>')
        
        node5 = ParentNode("div", None) #parent node (tag) with no children
        self.assertRaises(ValueError, node5.to_html)
        
        node6 = ParentNode(None, [LeafNode("p", "Hello, world!")]) #parent node (no tag) with a child leaf node (tag + value)
        self.assertRaises(ValueError, node6.to_html)
        

if __name__ == "__main__":
    unittest.main()