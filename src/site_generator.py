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
    with open(dest_path, "w") as f:
        f.write(html_file)
