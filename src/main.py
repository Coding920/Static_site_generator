import os
import sys
import shutil
from html_page_helpers import generate_pages_recursively

def main():
    try:
        base_path = sys.argv[1]
    except Exception:
        base_path = "/"

    if not os.path.exists("./docs"):
        os.mkdir("./docs")
    elif os.path.isfile("./docs"):
        os.remove("./docs")
        os.mkdir("./docs")
    elif os.listdir("./docs"):
        shutil.rmtree("./docs")
        os.mkdir("./docs")

    if not os.path.exists("./static"):
        raise ValueError("static dir missing")
    copy_files("./static", "./docs")
    generate_pages_recursively("./content", base_path, "./docs")

    return


def copy_files(src, dest):
    old_files = os.listdir(src)
    for file in old_files:
        file_path = f"{src}/{file}"
        if os.path.isfile(file_path):
            shutil.copy(file_path, f"{dest}/{file}")
        else:
            sub_dir = f"{src}/{file}"
            sub_dest = f"{dest}/{file}"
            os.mkdir(sub_dest)
            copy_files(sub_dir, sub_dest)
    return
    
main()
