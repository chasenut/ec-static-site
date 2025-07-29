from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    value = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, value)
        case TextType.BOLD:
            return LeafNode("b", value)
        case TextType.ITALIC:
            return LeafNode("i", value)
        case TextType.CODE:
            return LeafNode("code", value)
        case TextType.LINK:
            return LeafNode("a", value, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", value, {"src": text_node.url})
    raise Exception("Error, invalid TextNode.text_type of class TextType")
