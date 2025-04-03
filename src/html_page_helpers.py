import re
import os
from md_to_htmlnode import md_to_htmlnode

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if re.match(r"# \w", line) != None:
            return line.strip("# ")

    else:
        raise Exception("no title for file, must be found in the form of a h1 title")

def generate_page(src, template_path, dest):
    print(f"Generating page from {src} to {dest} using {template_path}")
    if not os.path.exists(src):
        raise Exception("Problem with source file/file not found")
    if not os.path.exists(template_path):
        raise Exception("Problem with template file/file not found")
    
    with open(src, "r") as f:
        source_file = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(source_file)
    source_html = md_to_htmlnode(source_file)
    source_html = source_html.to_html()
    template_with_title = template.replace("{{ Title }}", title)
    final_html = template_with_title.replace("{{ Content }}", source_html)
    with open(dest, "w") as f:
        f.write(final_html)
    return

def generate_pages_recursively(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise Exception("Source or destination directory doesn't exist")

    files = os.listdir(src_dir)
    for file in files:
        cur_file_path = f"{src_dir}/{file}"
        if os.path.isfile(cur_file_path) and file.endswith(".md"):
            html_file = f"{file.rstrip("md")}html"
            generate_page(cur_file_path, "template.html", f"{dest_dir}/{html_file}")
        else:
            os.mkdir(f"{dest_dir}/{file}")
            generate_pages_recursively(cur_file_path, f"{dest_dir}/{file}")

    return
