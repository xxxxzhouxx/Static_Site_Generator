from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.Text: #filter processed nodes
            new_nodes.append(node)
        else:
            original_text = node.text
            extracted_image = extract_markdown_images(original_text) # a list of tuples (image_alt, image_link)
            if extracted_image:
                for image_alt, image_link in extracted_image:
                    parts = original_text.split(f"![{image_alt}]({image_link})", 1)
                    if parts[0]!="":
                        new_nodes.append(TextNode(parts[0], TextType.Text))
                    new_nodes.append(TextNode(image_alt, TextType.Image, image_link))
                    original_text = parts[1] if len(parts) > 1 else ""
                if original_text!="": # Append any remaining text after the last image
                    new_nodes.append(TextNode(original_text, TextType.Text))
            else: #no image found, keep the original node
                new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.Text: #filter processed nodes
            new_nodes.append(node)
        else:
            original_text = node.text
            extracted_link = extract_markdown_links(original_text) # a list of tuples (link_text, link_url)
            if extracted_link:
                for link_text, link_url in extracted_link:
                    parts = original_text.split(f"[{link_text}]({link_url})", 1)
                    if parts[0]!="":
                        new_nodes.append(TextNode(parts[0], TextType.Text))
                    new_nodes.append(TextNode(link_text, TextType.Link, link_url))
                    original_text = parts[1] if len(parts) > 1 else ""
                if original_text!="": # Append any remaining text after the last link
                    new_nodes.append(TextNode(original_text, TextType.Text))
            else: #no link found, keep the original node
                new_nodes.append(node)
    return new_nodes
            

        