#!/usr/bin/python3

import sys
from csv import writer, reader
from os import walk as oswalk
from os import getcwd as osgetcwd
from os import lstat as oslstat
from os.path import join as path_join
from os.path import getmtime

#ARGS = {arg[0]: arg[1] for arg in enumerate(sys.argv[1:])}

# following needs a command line argument or it will error
#dirs = next(oswalk(ARGS[0]))[1]

def walk_dir(path=osgetcwd()):
    data = []
    for dir_path, dir_names, file_names in oswalk(path):
        for file in file_names:
            full_path = path_join(dir_path, file)
            data.append({"path":full_path, "last_modified":oslstat(full_path).st_mtime})

    return data

def read_dir_list(path=osgetcwd()):
    data = []
    with open(path_join(path, r".dir_list.csv"), "r", newline="\n") as f:
        lines = reader(f, delimiter=",")
        next(lines)
        for line in lines:
            data.append({line[0]: line[1]})

    return data

def csvwriter(data, path=osgetcwd()):
    with open(path_join(path, r".dir_list.csv"), "w+", newline="\n") as f:
        w = writer(f, delimiter=",")
        w.writerow(("path", "last_modified"))
        for line in data:
            w.writerow((line['path'], line['last_modified']))


FILES = walk_dir()
csvwriter(FILES)
for f in read_dir_list():
    print(f)
