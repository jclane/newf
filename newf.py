#!/usr/bin/python3

import sys
from csv import writer, reader
from os import walk as oswalk
from os import getcwd as osgetcwd
from os.path import join as path_join
from os.path import getmtime

from datetime import datetime # might not keep, just curious what file modfied/create times look like

#ARGS = {arg[0]: arg[1] for arg in enumerate(sys.argv[1:])}

# following needs a command line argument or it will error
#dirs = next(oswalk(ARGS[0]))[1]

def walk_dir(path=osgetcwd()):
    data = []
    for p in next(oswalk(path))[1]:
        data.append({"name":p, "last_modified":getmtime(p)})

    return data

def csvreader(path):
    data = []
    with open(path_join(path, r".dir_list.csv"), "w+", newline="\n") as f:
        lines = reader(f, delimiter=",")
        for line in lines:
            data.append({"name":line[0], "last_modified":line[1]})

    return data

def csvwriter(path, data):
    with open(path_join(path, r".dir_list.csv"), "w+", newline="\n") as f:
        w = writer(f, delimiter=",")
        for line in data:
            w.writerow((line['name'], line['last_modified']))
