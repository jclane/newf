#!/usr/bin/python3

import sys
from csv import writer, reader
from os import walk, getcwd, lstat
from os.path import exists, join, getmtime
from pprint import pprint


ARGS = {arg[0]: arg[1] for arg in enumerate(sys.argv[1:])}

def walk_dir(path):
    data = []
    for dir_path, dir_names, file_names in walk(path):
        for file in file_names:
            full_path = join(dir_path, file)
            data.append({"path":full_path, "last_modified":lstat(full_path).st_mtime})

    return data

def read_dir_list(path):
    PATH = join(path, r".dir_list.csv")
    data_dict = {}

    if exists(PATH):
        with open(PATH, "r", newline="\n") as f:
            lines = reader(f, delimiter=",")
            next(lines)
            for line in lines:
                data_dict[line[0]] = line[1]

    return data_dict

def csvwriter(data, path):
    with open(join(path, r".dir_list.csv"), "w+", newline="\n") as f:
        w = writer(f, delimiter=",")
        w.writerow(("path", "last_modified"))
        for line in data:
            w.writerow((line['path'], line['last_modified']))

def get_changes(files_list, csv_files_list):
    changes = {"added":[], "modified":[]}
    if len(csv_files_list.keys()):
        for el in files_list:
            if el["path"] in csv_files_list.keys():
                if str(el["last_modified"]) != csv_files_list[el["path"]]:
                    changes["modified"].append(el["path"])
            else:
                changes["added"].append(el["path"])
    else:
        changes["added"] = [el["path"] for el in files_list]

    return changes

def print_result(changes):
    print("\n")
    for k, v in changes.items():
        print(f"{k.upper()}:\n")
        for p in v:
            print(f"  {p}")
        print("\n")

def handle_args(args):
    if args:
        return {"path":ARGS[0]}
    return None

# parse command line arugments
args = handle_args(ARGS)
# set path to CLI argument or current working dir
PATH = args["path"] if args is not None and "path" in args.keys() else getcwd()
# get file names and paths and their last_modified time stamp
FILES = walk_dir(PATH)
# read the .dir_list.csv file if newf has been run before
FILES_CSV = read_dir_list(PATH)
# find the differences between the last run and this run
changes = get_changes(FILES, FILES_CSV)
print_result(changes)
# save details of the current path to .dir_list.csv
csvwriter(FILES, PATH)
