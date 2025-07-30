import re
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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        l = []
        text = node.text
        while len(text.split(delimiter, maxsplit=2)) > 2:
            phrases = text.split(delimiter, maxsplit=2)
            if phrases[0]:
                l.append(TextNode(phrases[0], TextType.TEXT))
            l.append(TextNode(phrases[1], text_type))
            text = phrases[2]
        if text:
            if delimiter in text:
                raise SyntaxError("Invalid Markdown syntax Error")
            l.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(l)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_images = extract_markdown_images(node.text)
        if not markdown_images and node.text:
            new_nodes.append(node)
            continue
        text = node.text
        l = []
        for image in markdown_images:
            parts = text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if parts[0]:
                l.append(TextNode(parts[0], TextType.TEXT))
            l.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = parts[1]
        if text:
            l.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(l)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_links = extract_markdown_links(node.text)
        if not markdown_links and node.text:
            new_nodes.append(node)
            continue
        text = node.text
        l = []
        for link in markdown_links:
            parts = text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            if parts[0]:
                l.append(TextNode(parts[0], TextType.TEXT))
            l.append(TextNode(link[0], TextType.LINK, link[1]))
            text = parts[1]
        if text:
            l.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(l)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
