from textnode import TextNode, TextType
from copy_static import copy_files_recursive
from site_generator import generate_pages_recursive
import os
import sys

static_path = "./static"
public_path = "./public"
template_path = "./template.html"
content_path = "./content"
public_path = "./docs"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    copy_files_recursive(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path, basepath)

if __name__ == "__main__":
    main()
