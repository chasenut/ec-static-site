import unittest
from conversions import (
    text_node_to_html_node,
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
)
from textnode import TextNode, TextType

class TestConversions(unittest.TestCase):
    def test_text_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_node2(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct_new_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, correct_new_nodes)

    def test_telim_bold(self):
        node = TextNode("This is text with **double** thic **bolds** texts within it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("double", TextType.BOLD),
            TextNode(" thic ", TextType.TEXT),
            TextNode("bolds", TextType.BOLD),
            TextNode(" texts within it", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, correct_new_nodes)

    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) ![image](https://github.com/chasenut/TF2-Sentry/blob/main/images/cad1.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://github.com/chasenut/TF2-Sentry/blob/main/images/cad1.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.google.com) ![link](https://github.com/chasenut)"
        )
        self.assertListEqual([("link", "https://www.google.com"), ("link", "https://github.com/chasenut")], matches)

