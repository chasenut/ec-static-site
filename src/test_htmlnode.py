import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")
        
    def test_repr2(self):
        node = HTMLNode("p")
        self.assertEqual(repr(node), "HTMLNode(p, None, None, None)")
        
    def test_repr3(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        node3 = HTMLNode("h1", "Front-end sucks", [node, node2])
        self.assertEqual(repr(node3), "HTMLNode(h1, Front-end sucks, [HTMLNode(p, None, None, None), HTMLNode(p, None, None, None)], None)")

    def test_repr4(self):
        node = HTMLNode("h1", "Front-end sucks", None, {"color": "red", "href": "https://www.google.com"})
        self.assertEqual(repr(node), "HTMLNode(h1, Front-end sucks, None, {'color': 'red', 'href': 'https://www.google.com'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me</a>")

    def test_leaf_to_html_a2(self):
        node = LeafNode("p", "Here we go", {"color": "blue", "font-family": "comic-sans"})
        self.assertEqual(node.to_html(), "<p color=\"blue\" font-family=\"comic-sans\">Here we go</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren2(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("a", "grandchild2", {"href": "https://www.google.com"})
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><a href=\"https://www.google.com\">grandchild2</a></span></div>",
        )

    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("a", "grandgrandchild", {"href": "https://www.google.com"})
        grandchild_node = ParentNode("b", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><a href=\"https://www.google.com\">grandgrandchild</a></b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
