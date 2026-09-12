from blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # split the raw document into block-level strings (headings, paragraphs, lists...)
    html_nodes_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.Heading:
            count = 0
            for letter in block:
                if letter == "#":
                    count += 1
                else:
                    break
            striped_block =block[count+1:] #remove the leading '#' characters and leading whitespace
            child_nodes = text_to_child_node(striped_block)
            node = ParentNode(f"h{count}", child_nodes, None) # Create an HTML node for a heading block without props
        elif block_type == BlockType.Code:
            striped_block = block[4:-3] # remove the leading and trailing "```" characters; and the leading newline character
            if striped_block[-1] == "\n": # remove the trailing newline character if it exists
                striped_block = striped_block[:-1]
            lines = striped_block.split('\n') # split the code block into lines
            clean_lines = [line.lstrip() for line in lines] # remove leading whitespace
            striped_block = "\n".join(clean_lines) # join the lines back together
            code_node = LeafNode("code", striped_block, None) # Create a LeafNode for the code block
            node = ParentNode("pre", [code_node], None) # Create a ParentNode for the code block without props         
        elif block_type == BlockType.Quote:
            lines = block.split('\n') # split the block into lines
            new_lines = []
            for line in lines:
                striped_line = line[1:] # remove the leading "> " characters
                clean_line = striped_line[1:] if striped_line.startswith(" ") else striped_line # remove the leading space if it exists
                new_lines.append(clean_line)
            child_nodes = text_to_child_node("\n".join(new_lines))
            node = ParentNode("blockquote", child_nodes, None)
        elif block_type == BlockType.Unordered_list:
            lines = block.split('\n') # split the block into lines
            nodes = []
            for line in lines:
                striped_line = line[2:] # remove the leading "- " characters
                child_nodes = text_to_child_node(striped_line)
                one_line_node = ParentNode("li", child_nodes, None)
                nodes.append(one_line_node)
            node = ParentNode("ul", nodes, None) # Create a parent node for the entire unordered list
        elif block_type == BlockType.Ordered_list:
            lines = block.split('\n') # split the block into lines
            nodes = []
            for line in lines:
                while line[0].isdigit():
                    line = line[1:] # remove leading digits
                striped_line = line[2:] # remove the leading ". "
                one_line_children = text_to_child_node(striped_line)
                one_line_node = ParentNode("li", one_line_children, None)
                nodes.append(one_line_node)
            node = ParentNode("ol", nodes, None)
        elif block_type == BlockType.Paragraph:
            lines = block.split('\n') # split the block into lines
            clean_lines = [line.lstrip() for line in lines] # remove leading whitespace
            block = " ".join(clean_lines) # join the lines back together
            child_nodes = text_to_child_node(block)
            node = ParentNode("p", child_nodes, None)
        html_nodes_children.append(node)
        html_node = ParentNode("div", html_nodes_children, None) # Create a parent node for the entire document
    return html_node

def text_to_child_node(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for text_node in text_nodes:
        if isinstance(text_node, TextNode):
            child_node = text_node_to_html_node(text_node) # create a proper leaf node based on the TextNode's type, text, and url
            child_nodes.append(child_node)
    return child_nodes
