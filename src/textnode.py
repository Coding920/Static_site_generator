from enum import Enum

class TextType(Enum):
    Normal = "normal"
    Bold = "bold"
    Italic = "italic"
    Code = "code"
    Link = "link"
    Image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if type(text_type) != TextType:
            raise Exception("Text_type must be of Enum TextType")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.url == other.url
            and self.text == other.text
            and self.text_type == other.text_type)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    
