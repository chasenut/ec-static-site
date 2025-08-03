from textnode import TextNode, TextType
from copy_static import copy_files_recursive
import os

static_path = "./static"
public_path = "./public"

def main():
    textNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textNode)
    copy_files_recursive(static_path, public_path)


if __name__ == "__main__":
    main()
