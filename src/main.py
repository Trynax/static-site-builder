from textnode import TextNode

def main():
    text_node = TextNode("This is a test", "italic", "www.example.com")
    print(text_node.__repr__())


main()