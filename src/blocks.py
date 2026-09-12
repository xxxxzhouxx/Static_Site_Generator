from enum import Enum

def markdown_to_blocks(markdown): # split a string into blocks based on double newlines, and remove empty blocks
    blocks = markdown.split('\n\n')
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if not blocks[i]:
            del blocks[i]
            i -= 1
    return blocks


class BlockType(Enum):
    Paragraph = "paragraph"
    Heading = "heading"
    Code = "code"
    Quote = "quote"
    Unordered_list = "unordered_list"
    Ordered_list = "ordered_list"

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.Heading
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.Code
    elif block.startswith("> "):
        return BlockType.Quote
    elif block.startswith("- "):
        return BlockType.Unordered_list
    elif block.split()[0].endswith(".") and block.split()[0][0].isdigit():
        return BlockType.Ordered_list
    else:
        return BlockType.Paragraph
