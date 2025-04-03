
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
        for split in node_splits:
            if not split:
                continue    
            if (split.startswith(" ") or split.endswith(" ")
            or split.startswith(".") or split.startswith(",")
            or split.startswith(":") or split.startswith(";")
            or split.startswith(")")):
                new_nodes.append(TextNode(text=split, text_type=TextType.Normal))
            else:
                new_nodes.append(TextNode(text=split, text_type=text_type))

    return new_nodes

def configure_extracter(regex):
    def extracter(text) -> list[tuple]:
        extracted_info = re.findall(regex, text)
        return extracted_info
    return extracter

extract_md_images = configure_extracter(r"!\[(.*?)\]\((.*?)\)")
extract_md_links = configure_extracter(r"\[(.*?)\]\((.*?)\)")

def split_nodes_configurer(function, text_type):
    def split_nodes(old_nodes) -> list[TextNode]:
        new_nodes = []
        for node in old_nodes:
            if function(node.text) == []:
                new_nodes.append(node)
                continue

            link_info = function(node.text)
            current_link = link_info[0]
            split_text = node.text.split(f"{"!" if text_type == TextType.Image else ""}[{current_link[0]}]({current_link[1]})")

            if split_text[0].strip():
                new_nodes.append(TextNode(text=split_text[0], text_type=TextType.Normal))

            new_nodes.append(TextNode(text=current_link[0], text_type=text_type, url=current_link[1]))

            if len(split_text) > 1 and split_text[1]:
                remaining_nodes = split_nodes([TextNode(text=split_text[1], text_type=TextType.Normal)])
                new_nodes.extend(remaining_nodes)

        return new_nodes

    return split_nodes

split_nodes_images = split_nodes_configurer(extract_md_images, TextType.Image)
split_nodes_links = split_nodes_configurer(extract_md_links, TextType.Link)

# Recursive version Wip
# ef split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
#    new_nodes = []

#    for node in old_nodes:
#        if delimiter not in node.text or node.text_type != TextType.Normal:
#            new_nodes.append(node)
#            continue

#        if node.text.count(delimiter) % 2 != 0:
#            raise Exception(f"invalid markdown syntax, missing closing {delimiter}")

#        split_text = node.text.split(delimiter)
#        for section in split_text:
#            print(section)
#            if not section[0]:
#                new_nodes.append(TextNode(text=section[1], text_type=text_type))
#                new_nodes.extend(split_nodes_delimiter([TextNode(text=section[3], text_type=TextType.Normal)], delimiter, text_type))
#            elif section[0]:
#                new_nodes.append(TextNode(text=section[0], text_type=TextType.Normal))
#                new_nodes.append(TextNode(text=section[1], text_type=text_type))
#                new_nodes.extend(split_nodes_delimiter([TextNode(text=section[2], text_type=TextType.Normal)], delimiter, text_type))

#    return new_nodes

