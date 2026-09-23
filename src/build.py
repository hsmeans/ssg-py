# Yes I could have used shutil.copytree, but I like having fun sometimes.

import os
import shutil

STATIC_DIR = "static/"
PUBLIC_DIR = "public/"


def build_file(file: str, public_pwd: str):
    print("COPY", file, public_pwd)
    shutil.copy(file, public_pwd)


def build_dir(static_pwd: str, public_pwd: str):
    print("BUILD", static_pwd, public_pwd)
    if not os.path.exists(public_pwd):
        os.mkdir(public_pwd)
    for path in os.listdir(static_pwd):
        full_path = os.path.join(static_pwd, path)
        if os.path.isfile(full_path):
            build_file(full_path, public_pwd)
        else:
            build_dir(full_path, os.path.join(public_pwd, path))


def build():
    if not os.path.exists(STATIC_DIR):
        raise Exception("No static/ directory present")
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.mkdir(PUBLIC_DIR)
    build_dir(STATIC_DIR, PUBLIC_DIR)
