from enum import Enum

class BlockType(Enum):
    Paragraph = "paragraph"
    Heading = "heading"
    Code = "code"
    Quote = "quote"
    OL = "ordered list"
    UL = "unordered list"

def block_to_block_type(block) -> BlockType:
    if block.startswith("#"):
        heading_size = block.count("#")
        if block[:heading_size + 1] == "#" * heading_size + " ":
            return BlockType.Heading
    if block.startswith("```") and block.endswith("```"):
        return BlockType.Code
    if block.startswith(">"):
        if lines_start_with(block, ">"):
            return BlockType.Quote
    if block.startswith("- "):
        if lines_start_with(block, "- "):
            return BlockType.UL
    if block.startswith("1. "):
        lines = block.splitlines()
        correct = True
        for idx, line in enumerate(lines):
            if not line.startswith(f"{idx + 1}. "):
                correct = False
        if correct:
            return BlockType.OL
    return BlockType.Paragraph



def lines_start_with(block, symbol) -> bool:
    lines = block.splitlines()
    all_start = True
    for line in lines:
        if not line.startswith(symbol):
            all_start = False
    return all_start
