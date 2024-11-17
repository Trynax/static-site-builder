from enum import Enum

class TextType(Enum):
    TEXT="text"
    BOLD="bold"
    ITALIC="italic"
    CODE="code"
    LINK="link"
    IMAGE="image"

class TextNode:
    def __init__(self, text,text_type,text_url=None):
        self.text = text
        self.text_type = text_type
        self.text_url = text_url
    def __eq__(self, value):
        if self.text_type == value.text_type and (self.text==value.text and self.text_url==value.text_url):
            return True
    def __repr__(self):
        return f'TextNode({self.text},{self.text_type},{self.text_url})'
    