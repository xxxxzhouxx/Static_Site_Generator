from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.Text: #filter processed nodes
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter) #split the text by the delimiter
            if len(parts) % 2 == 0: #even number of parts means unmatched delimiter
                raise ValueError(f"Invalid Markdown syntax: Unmatched delimiter '{delimiter}' in text '{node.text}'")
            for index in range(len(parts)):
                if parts[index] == "": #skip empty parts
                    continue
                if index % 2 == 0: #even index means plain text
                    new_nodes.append(TextNode(parts[index], TextType.Text))
                else: #odd index means formatted text
                    new_nodes.append(TextNode(parts[index], text_type))
    return new_nodes