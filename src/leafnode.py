from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Leaf node must have a value')
        if self.tag is None:
            return f'{self.value}'
        else:
            s = f'<{self.tag} '
            if self.props is not None:
                props = self.props_to_html()
                s += f' {props}'
            s += f'>{self.value}</{self.tag}>'
            return s