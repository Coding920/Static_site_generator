import os
import shutil

def main():
    if not os.path.exists("./public"):
        os.mkdir("./public")
    elif os.path.isfile("./public"):
        os.remove("./public")
        os.mkdir("./public")
    elif os.listdir("./public"):
        shutil.rmtree("./public")
        os.mkdir("./public")

    if not os.path.exists("./static"):
        raise ValueError("static dir missing")
    copy_files("./static", "./public")

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
