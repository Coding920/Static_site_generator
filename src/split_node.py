
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
            if split.startswith(" ") or split.endswith(" "):
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
            
            # Split text on info
            image_info = function(node.text)
            for pair in image_info:
                sections = node.text.split(f"{"!" if text_type == TextType.Image else ""}[{pair[0]}]({pair[1]})", 1)
                sections = list(filter(lambda item: item if not item.isspace() else "", sections))
                sections = list(filter(lambda item: item, sections))
                if len(sections) == 1 and sections[0].startswith(" "):
                    new_nodes.extend(
                            [TextNode(text=pair[0], text_type=text_type, url=pair[1]),
                             TextNode(text=sections[0], text_type=TextType.Normal)])
                elif len(sections) < 2 and sections[0].endswith(" "):
                    new_nodes.extend([
                        TextNode(text=sections[0], text_type=TextType.Normal),
                        TextNode(text=pair[0], text_type=text_type, url=pair[1])])
                else:
                    new_nodes.extend([
                        TextNode(text=sections[0], text_type=TextType.Normal),
                        TextNode(text=pair[0], text_type=text_type, url=pair[1]),
                        TextNode(text=sections[1], text_type=TextType.Normal)])

        return new_nodes
    return split_nodes

split_nodes_images = split_nodes_configurer(extract_md_images, TextType.Image)
split_nodes_links = split_nodes_configurer(extract_md_links, TextType.Link)
