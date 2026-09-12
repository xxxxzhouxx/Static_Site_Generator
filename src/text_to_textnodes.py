from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from inline_markdown import extract_markdown_images, extract_markdown_links
from split_images_links import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.Text, None)] # create a single item TextNode list with the entire text as its content and TextType.Text as its type
    nodes = split_nodes_delimiter(nodes, "**", TextType.Bold) # split the node based on the delimiter and TextType
    nodes = split_nodes_delimiter(nodes, "_", TextType.Italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.Code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


