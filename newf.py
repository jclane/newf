#!/usr/bin/python3

import sys
from csv import writer, reader
from os import walk as oswalk
from os.path import join as path_join

ARGS = {arg[0]: arg[1] for arg in enumerate(sys.argv[1:])}

# following needs a command line argument or it will error
dirs = next(oswalk(ARGS[0]))[1]

def csvreader():
    data = []
    with open(path_join(ARGS[0], r".dir_list.csv"), "r", newline="\n") as f:
        lines = reader(f, delimiter=",")
        for line in lines:
            data.append(line)

    return data

def csvwriter(data):
    with open(path_join(ARGS[0], r".dir_list.csv"), "w+", newline="\n") as f:
        w = writer(f, delimiter=",")
        for line in data:
            print(line)
            w.writerow(line)

csvwriter([["docs"], ["pics"], ["books"], ["bin"]])
data = csvreader()
#print(data)
