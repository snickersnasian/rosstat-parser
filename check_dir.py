import os

def check_and_create_dir(dirname):
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

def check_dirs(dirnames):
    for dirname in dirnames:
        check_and_create_dir(dirname)


