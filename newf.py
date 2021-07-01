#!/usr/bin/python3

import sys
from csv import writer, reader
from os import walk, getcwd, lstat
from os.path import join, getmtime


#ARGS = {arg[0]: arg[1] for arg in enumerate(sys.argv[1:])}
def walk_dir(path=getcwd()):
    data = []
    for dir_path, dir_names, file_names in walk(path):
        for file in file_names:
            full_path = join(dir_path, file)
            data.append({"path":full_path, "last_modified":lstat(full_path).st_mtime})

    return data

def read_dir_list(path=getcwd()):
    data_dict = {}
    with open(join(path, r".dir_list.csv"), "r", newline="\n") as f:
        lines = reader(f, delimiter=",")
        next(lines)
        for line in lines:
            data_dict[line[0]] = line[1]

    return data_dict

def csvwriter(data, path=getcwd()):
    with open(join(path, r".dir_list.csv"), "w+", newline="\n") as f:
        w = writer(f, delimiter=",")
        w.writerow(("path", "last_modified"))
        for line in data:
            w.writerow((line['path'], line['last_modified']))

def get_changes(files_list, csv_files_list):
    changes = []
    for el in files_list:
        if el["path"] in csv_files_list.keys():
            if el["last_modified"] != csv_files_list[el["path"]]:
                changes.append(el)
        else:
            print(f"File was added!: {el['path']}")
            changes.append(el)

    return changes


FILES = walk_dir()
FILES_CSV = read_dir_list()

print(len(get_changes(FILES, FILES_CSV)))

csvwriter(FILES)
