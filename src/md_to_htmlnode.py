from htmlnode import HTMLNode, ParentNode, LeafNode
from md_to_blocks import md_to_blocks
from blocktype import BlockType, block_to_block_type
from text_to_textnode import text_to_textnodes
from text_to_htmlnode import text_node_to_html_node


def md_to_htmlnode(text) -> HTMLNode:
    if not text or type(text) != str:
        raise ValueError("md_to_htmlnode takes non-empty str")

    new_nodes = []
    blocks = md_to_blocks(text)

    for block in blocks:
        block_type = block_to_block_type(block)
        
        match block_type:
            case BlockType.Heading:
                new_nodes.append(heading_block_to_html(block))
            case BlockType.Quote:
                new_nodes.append(quote_block_to_html(block))
            case BlockType.Code:
                new_nodes.append(code_block_to_html(block))
            case BlockType.OL:
                new_nodes.append(olist_block_to_html(block))
            case BlockType.UL:
                new_nodes.append(ulist_block_to_html(block))
            case BlockType.Paragraph:
                new_nodes.append(paragraph_block_to_html(block))
            case _:
                raise ValueError("You shouldn't be here")
    
    div_parent = ParentNode(tag="div", children=new_nodes)

    return div_parent


def heading_block_to_html(block):
    heading_size = block.count("#", 0, 6)
    new_block = block.lstrip("# ")
    return ParentNode(tag=f"h{heading_size}", children=text_to_children(new_block))

def quote_block_to_html(block):
    lines = block.splitlines()
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip("> "))
    new_block = "\n".join(new_lines)
    return ParentNode(tag="blockquote", children=text_to_children(new_block))

def code_block_to_html(block):
    block = block.lstrip("```\n").rstrip("```")
    code_parent_node = ParentNode(tag="code", children=[LeafNode(value=block)])
    return ParentNode(tag="pre", children=[code_parent_node])

def list_to_html_configure(tag):
    def list_block_to_html(block):
        lines = block.splitlines()
        children = []
        for line in lines:
            line = line.lstrip("0123456789.- ")
            children.append(ParentNode(tag="li", children=text_to_children(line)))

        ol_html = ParentNode(tag=tag, children=children)
        return ol_html
    return list_block_to_html

olist_block_to_html = list_to_html_configure("ol")
ulist_block_to_html = list_to_html_configure("ul")

def paragraph_block_to_html(block):
    block = block.replace("\n", " ")
    return ParentNode(tag="p", children=text_to_children(block))

def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
