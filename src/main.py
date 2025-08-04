from textnode import TextNode, TextType
from copy_static import copy_files_recursive
from site_generator import generate_page
import os

static_path = "./static"
public_path = "./public"
template_path = "./template.html"

def main():
    copy_files_recursive(static_path, public_path)
    generate_page("./content/index.md", template_path, "./public/index.html")

if __name__ == "__main__":
    main()
