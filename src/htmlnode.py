
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        attributes = ""
        for attr, data in self.props.items():
            attributes += f" {attr}=\"{data}\""

        return attributes

    def __repr__(self):
        return f"{self.tag=}\n{self.value=}\n{self.children=}\n{self.props=}"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None): # No children
        if value == None:
            raise ValueError("Leaf nodes must have value")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props=None): # No text values
        if tag == None:
            raise ValueError("Parent Node must have tag")
        if children == []:
            raise ValueError("Parent must have children")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{"".join(list(map(lambda item: item.to_html(), self.children)))}</{self.tag}>"


