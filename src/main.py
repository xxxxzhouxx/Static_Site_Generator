from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_html_node
from pathlib import Path
import os
import shutil

def main():
    markdown = "# This is a **TITLE**"
    title = extract_title(markdown)
    print(title)
    check_target_directory("./public")
    copy_files("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


def check_target_directory (target_directory: str): # verify the existence of the target_directory; get an empty directory ready
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory) # delete the target_directory
    os.mkdir(target_directory) # create an empty target_directory

def copy_files(source_directory: str, target_directory: str): # copy everything from source_directory to target_directory
    items = os.listdir(source_directory) # get the list of items in the source_directory
    for item in items:
        source_path = os.path.join(source_directory, item) # get the full path of the item in the source_directory
        target_path = os.path.join(target_directory, item) # get the full path of the item in the target_directory
        if os.path.isdir(source_path): # if the item is a directory, recursively call the function
            os.mkdir(target_path) # create the directory in the target_directory
            copy_files(source_path, target_path) # recursively copy the contents of the directory
        else:
            shutil.copy(source_path, target_path) # copy the file to the target_directory

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):  # Check for a level 1 heading
            return line[2:].strip()  # Return the title without the '# ' prefix
    raise Exception("No title found in the markdown content.")

def generate_page(from_path, template_path, dest_path): #generate a single HTML page from a markdown file and a template
    print (f"Generating page from {from_path} to {dest_path} using template {template_path}")
    content = Path(from_path).read_text()  # Read the markdown content from the source file
    template = Path(template_path).read_text()  # Read the template content from the template file
    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()
    title = extract_title(content)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)  # Ensure the destination directory exists
    Path(dest_path).write_text(final_html) # write the HTML content to the file

def generate_pages_recursive(dir_path_content, template_path, dest_dir_push):
    items = os.listdir(dir_path_content) # get the list of items in the content directory
    for item in items:
        source_path = os.path.join(dir_path_content, item) # get the full path of the item in the content directory
        if os.path.isdir(source_path): # if the item is a directory, recursively call the function
            dest_path = os.path.join(dest_dir_push, item) # get the full path of the item in the destination directory
            os.makedirs(dest_path, exist_ok=True) # create the directory in the destination directory
            generate_pages_recursive(source_path, template_path, dest_path)
        if os.path.isfile(source_path): # the item is a file, generate the page
            file_name = os.path.splitext(item)[0] # get the file name without extension
            dest_path = os.path.join(dest_dir_push, file_name + ".html") # create the destination path with .html extension
            generate_page(source_path, template_path, dest_path)



main()


        