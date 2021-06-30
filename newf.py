#!/usr/bin/python3

import sys
from csv import writer, reader
from os import walk as oswalk
from os import getcwd as osgetcwd
from os.path import join as path_join

#ARGS = {arg[0]: arg[1] for arg in enumerate(sys.argv[1:])}

# following needs a command line argument or it will error
#dirs = next(oswalk(ARGS[0]))[1]

class DirectoryListHandler:

    dir_list = []

    def __init__(self, path=osgetcwd()):
        self.path = path
        self.dirs = next(oswalk(path))[1]
        self.dir_list = self.csvreader()

    def get_mtime(self, file):
        print(file)

    def csvreader(self):
        data = []
        with open(path_join(self.path, r".dir_list.csv"), "w+", newline="\n") as f:
            lines = reader(f, delimiter=",")
            for line in lines:
                print(os.path.getmtime(line))
                data.append({"name":line})

        return data

def csvwriter(path):
    with open(path_join(path, r".dir_list.csv"), "w+", newline="\n") as f:
        w = writer(f, delimiter=",")
        for line in data:
            w.writerow(line)


dl = DirectoryListHandler()

