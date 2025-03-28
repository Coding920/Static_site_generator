
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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

