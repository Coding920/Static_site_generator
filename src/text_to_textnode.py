from split_node import split_nodes_images, split_nodes_links, split_nodes_delimiter
from textnode import TextType, TextNode

def text_to_textnodes(text) -> list[TextNode]:
    first_node = TextNode(text=text, text_type=TextType.Normal)

    list_has_changed = True
    node_list = [first_node]
    while list_has_changed == True:
        list_before = node_list.copy()
        node_list = split_nodes_images(node_list)
        node_list = split_nodes_links(node_list)
        node_list = split_nodes_delimiter(node_list, "`", text_type=TextType.Code)
        node_list = split_nodes_delimiter(node_list, "**", text_type=TextType.Bold)
        node_list = split_nodes_delimiter(node_list, "_", text_type=TextType.Italic)
        if node_list == list_before:
            list_has_changed = False

    return node_list

