
import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        if delimiter not in node.text or node.text_type != TextType.Normal:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"invalid markdown syntax, missing closing {delimiter}")

        node_splits = node.text.split(delimiter)
        for idx, split in enumerate(node_splits):
            if idx % 2 == 0:
                new_nodes.append(TextNode(split, TextType.Normal))
            else:
                new_nodes.append(TextNode(split, text_type))

    return new_nodes

def extract_md_images(text) -> list[tuple]:
    image_info = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_info

def extract_md_links(text) -> list[tuple]:
    link_info = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_info
