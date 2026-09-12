import unittest
from split_images_links import split_nodes_image, split_nodes_link

def test_split_images(self):
    node1 = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node1])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ],
        new_nodes,
    )

def test_split_links(self):
    node2 = TextNode(
        "This is text with a [link](https://www.boot.dev) and another [second link](https://www.github.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node2])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://www.github.com"),
        ],
        new_nodes,
    )