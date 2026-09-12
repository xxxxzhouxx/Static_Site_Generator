from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    Text = "text"
    Bold = "bold"
    Italic = "italic"
    Code = "code"
    Link = "link"
    Image = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode(self.text, self.text_type, self.url)"
    
    # Convert a TextNode to a LeafNode based on the tag (Text_Type of TextNode), value (Text of TextNode), and props (url of TextNode) of the TextNode.
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match (text_node.text_type):
        case TextType.Text:
            return LeafNode(None, text_node.text)
        case TextType.Bold:
            return LeafNode("b", text_node.text)
        case TextType.Italic:
            return LeafNode("i", text_node.text)
        case TextType.Code:
            return LeafNode("code", text_node.text)
        case TextType.Link:
            if text_node.url is None:
                raise ValueError("Link TextNode must have a url")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.Image:
            if text_node.url is None:
                raise ValueError("Image TextNode must have a url")
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Unknown TextType")
