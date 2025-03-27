from textnode import TextNode, TextType

def main():
    test = TextNode("this is some anchor text", TextType.Link, "https://www.boot.dev")
    print(test)

main()
