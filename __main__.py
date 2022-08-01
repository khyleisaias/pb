#!/usr/bin/env python3

import os
import subprocess

""" PB: A New Build System """
""" NOTE: Pybuild is a failed project, so I'm making a new one. """
ip = 0
def cat(cur_file):
    with open(cur_file, 'r') as f:
        return f.read()
def files(file_list):
    global ip
    fl = file_list.split(" ")
    for ip in range(len(fl)):
        if os.path.exists(fl[ip]):
            cur_file = fl[ip]
            print(f"`{fl[ip]}` exist, you can use the file")
            print(cat(cur_file))
        else:
            print(f"`{fl[ip]}` does not exist, you cannot continue")
            exit(1)
        ip += 1
    ip += 1

files("__main__.py")

