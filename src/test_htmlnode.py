import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode('b', 'bold text')
        self.assertEqual(print(node), print('HTMLNode("b", "bold text)'))

    def test_repr2(self):
        node = HTMLNode('b', 'bold text')
        self.assertEqual(print(node), print('HTMLNode("b", "bold text)'))


if __name__ == "__main__":
    unittest.main()
