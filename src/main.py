from textnode import TextNode, TextType
from copy_static import copy_files_recursive
from site_generator import generate_pages_recursive
import os

static_path = "./static"
public_path = "./public"
template_path = "./template.html"
content_path = "./content"
public_path = "./public"

def main():
    copy_files_recursive(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == "__main__":
    main()
