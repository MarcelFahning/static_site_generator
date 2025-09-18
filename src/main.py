from textnode import TextNode, TextType


def main():
    node = TextNode('This is a text node', TextType.LINK, 'https://www.boot.dev')
    print(node)

main()