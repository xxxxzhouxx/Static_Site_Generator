import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        HTMLNode1 = HTMLNode(tag="div", value=None, children=[], props={"href": "https://www.boot.dev", "target": "_blank"})
        HTMLNode2 = HTMLNode(tag="a", value="Click here", children=[], props={"href": "https://www.boot.dev", "target": "_blank"})
        HTMLNode3 = HTMLNode(tag="p", value="This is a paragraph", children=[], props={})
        HTMLNode4 = HTMLNode(tag="span", value="This is a span", children=[], props={})
        HTMLNode5 = HTMLNode(tag="ul", value=None, children=[], props={})
        HTMLNode1.props_to_html()
        HTMLNode2.props_to_html()
        HTMLNode3.props_to_html()
        HTMLNode4.props_to_html()
        HTMLNode5.props_to_html()

if __name__ == "__main__":
    unittest.main()