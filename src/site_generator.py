from block_convs import markdown_to_html_node
from htmlnode import ParentNode
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            text = line[2:].strip()
            return text
    raise SyntaxError("No page title found (h1 header)")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = ""
    with open(from_path, "r") as f:
        from_file = f.read()
    html_file = ""
    with open(template_path, "r") as f:
        html_file = f.read()

    title = extract_title(from_file)
    content  = markdown_to_html_node(from_file).to_html()

    html_file = html_file.replace("{{ Title }}", title)
    html_file = html_file.replace("{{ Content }}", content)

    dirname = os.path.dirname(dest_path)
    os.makedirs(dirname, exist_ok=True)

    dest_path = dest_path.rstrip(".md")
    dest_path += ".html"

    with open(dest_path, "w") as f:
        f.write(html_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        content = os.path.join(dir_path_content, entry)
        destination = os.path.join(dest_dir_path, entry)
        if os.path.isdir(content):
            generate_pages_recursive(content, template_path, destination)
        else:
            generate_page(content, template_path, destination)

