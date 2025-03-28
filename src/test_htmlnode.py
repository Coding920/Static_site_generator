import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode.to_html(self)

    def test_repr_func(self):
        node = HTMLNode(tag="p", value="pleh", children="left, right", props={"href": "test/styles.css"})
        self.assertEqual(node.__repr__(), "self.tag='p'\nself.value='pleh'\nself.children='left, right'\nself.props={'href': 'test/styles.css'}")

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "styles.css", "src": "example.com"})
        self.assertEqual(node.props_to_html(), " href=\"styles.css\" src=\"example.com\"")
        
    def test_leaf_to_html(self):
        leaf = LeafNode("p", "Hello, world!")
        self.assertEqual(leaf.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        leaf = LeafNode("a", "Boot.dev", props={"href": "www.boot.dev", "target": "_blank"})
        self.assertEqual(leaf.to_html(), "<a href=\"www.boot.dev\" target=\"_blank\">Boot.dev</a>")

    def test_leaf_error(self):
        with self.assertRaises(ValueError):
            LeafNode()

    def test_parent_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="test")

    def test_parent_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(children=[HTMLNode()])

    def test_parent_with_child(self):
        child = LeafNode(tag="p", value="child")
        parent = ParentNode(tag="div", children=[child])
        self.assertEqual(
                parent.to_html(),
            "<div><p>child</p></div>"
        )

    def test_parent_with_grandchild(self):
        child = LeafNode(tag="p", value="child")
        parent = ParentNode(tag="div", children=[child])
        grandparent = ParentNode(tag="html", children=[parent])
        self.assertEqual(
                grandparent.to_html(),
            "<html><div><p>child</p></div></html>"
        )

    def test_parent_with_props(self):
        child = LeafNode(tag="p", value="child")
        parent = ParentNode(tag="div", children=[child], props={"href": "www.boot.dev", "target": "_blank"})
        self.assertEqual(
                parent.to_html(),
            "<div href=\"www.boot.dev\" target=\"_blank\"><p>child</p></div>"
        )

    def test_child_with_props(self):
        child = LeafNode(tag="p", value="child", props={"href": "www.boot.dev", "target": "_blank"})
        parent = ParentNode(tag="div", children=[child])
        self.assertEqual(
                parent.to_html(),
            "<div><p href=\"www.boot.dev\" target=\"_blank\">child</p></div>"
        )

    def test_child_and_parent_with_props(self):
        child = LeafNode(tag="p", value="child", props={"href": "www.boot.dev", "target": "_blank"})
        parent = ParentNode(tag="div", children=[child], props={"href": "www.boot.dev", "target": "_blank"})
        self.assertEqual(
                parent.to_html(),
            "<div href=\"www.boot.dev\" target=\"_blank\"><p href=\"www.boot.dev\" target=\"_blank\">child</p></div>"
        )

    def test_parent_with_children(self):
        child_header = LeafNode(tag="h1", value="header")
        child_para = LeafNode(tag="p", value="paragraph")
        parent = ParentNode(tag="div", children=[child_header, child_para])
        self.assertEqual(
                parent.to_html(),
            "<div><h1>header</h1><p>paragraph</p></div>"
        )

    def test_parent_with_children(self):
        child_header = LeafNode(tag="h1", value="header")
        child_para = LeafNode(tag="p", value="paragraph")
        parent_div = ParentNode(tag="div", children=[child_header, child_para])
        parent_span = ParentNode(tag="span", children=[child_header, child_para])
        grandparent = ParentNode(tag="div", children=[parent_div, parent_span])
        self.assertEqual(
                grandparent.to_html(),
            "<div><div><h1>header</h1><p>paragraph</p></div><span><h1>header</h1><p>paragraph</p></span></div>"
        )


if __name__ == "__main__":
    unittest.main()
