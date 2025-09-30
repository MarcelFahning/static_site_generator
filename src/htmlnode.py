class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        result = []
        for key, val in self.props.items():
            result.append(f'{key}="{val}"')
        return " " + " ".join(result)

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> str:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Leaf node must have a value')
        if self.tag is None:
            return f'{self.value}'
        else:
            s = f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            return s

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag, None, list, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError('no tag provided')
        if self.children is None:
            raise ValueError('no children provided')

        result = f'<{self.tag}'
        for child in self.children:
            result += child.to_html()
        result += f'</{self.tag}>'

        return result