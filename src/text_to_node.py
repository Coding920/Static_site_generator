from enum import Enum
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node: TextNode):
    if type(text_node) != TextNode:
        raise ValueError("text_node must be of class TextNode")

    match text_node.text_type:
        case TextType.Normal:
            return normal_to_leafnode(text_node.text)

        case TextType.Bold:
            return bold_to_leafnode(text_node.text)

        case TextType.Italic:
            return italic_to_leafnode(text_node.text)

        case TextType.Link:
            return link_to_leafnode(text_node.text, text_node.url)

        case TextType.Image:
            return image_to_leafnode(text_node.url, text_node.text)


def configure_tag(tag=None):
    def to_leafnode(value):
        return LeafNode(tag=tag, value=value)
    return to_leafnode

normal_to_leafnode = configure_tag()
bold_to_leafnode = configure_tag("b")
italic_to_leafnode = configure_tag("i")

def link_to_leafnode(value, link):
    return LeafNode(tag="a", value=value, props={"href": link})

def image_to_leafnode(src, alt):
    return LeafNode(tag="img", value="", props={"src": src, "alt": alt})
