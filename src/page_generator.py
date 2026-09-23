import os

from converter import markdown_to_html_node
from title_extraction import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path):
        raise ValueError("from_path must be a path to a valid file")
    if not os.path.exists(template_path):
        raise ValueError("template_path must be a path to a valid file")
    md, template = None, None
    with open(from_path) as mdfile:
        md = mdfile.read()
    with open(template_path) as template_file:
        template = template_file.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    dest_content = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace('src="/', f'src="{basepath}')
        .replace('href="/', f'href="{basepath}')
    )

    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w") as dest:
        dest.write(dest_content)


def generate_page_recursively(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str
):
    if not os.path.exists(dir_path_content):
        raise ValueError("dir_path_content must exist")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for path in os.listdir(dir_path_content):
        full_content_path = os.path.join(dir_path_content, path)
        full_dest_path = os.path.join(dest_dir_path, path)
        if os.path.isfile(full_content_path):

            generate_page(
                full_content_path,
                template_path,
                f"{os.path.splitext(full_dest_path)[0]}.html",
                basepath,
            )
        else:
            generate_page_recursively(
                full_content_path, template_path, full_dest_path, basepath
            )
