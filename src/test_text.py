import unittest
from textnode import TextNode, TextType

def test_text_to_textnodes(self):
    text = "This is a **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.bootdev.com)"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is a ", TextType.Text),
            TextNode("bold", TextType.Bold),
            TextNode(" text with an ", TextType.Text),
            TextNode("image", TextType.Image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("and a ", TextType.Text),
            TextNode("link", TextType.Link, "https://www.bootdev.com"),
        ],
        nodes,
    )

def test_text_to_textnodes(self):
    text = "This is a _italic text with an_ ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.bootdev.com)"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is a ", TextType.Text),
            TextNode("italic text with an", TextType.Italic),
            TextNode("image", TextType.Image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("and a ", TextType.Text),
            TextNode("link", TextType.Link, "https://www.bootdev.com"),
        ],
        nodes,
    )

def test_text_to_textnodes(self):
    text = "![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.bootdev.com)"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("image", TextType.Image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("and a ", TextType.Text),
            TextNode("link", TextType.Link, "https://www.bootdev.com"),
        ],
        nodes,
    )