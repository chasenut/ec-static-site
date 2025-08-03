import os
import shutil

def copy_files_recursive(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    for filename in os.listdir(src_path):
        src = os.path.join(src_path, filename)
        dst = os.path.join(dst_path, filename)
        print(f"Copying {src} -> {dst}")
        if os.path.isfile(src):
            shutil.copy(src, dst)
            continue
        copy_files_recursive(src, dst)
