#!/usr/bin/env python

import os
import argparse
import json
import os.path

def enumeratePaths(path):
    """Returns the path to all the files in a directory as a list"""
    file_list = {}
    file_collection = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            filesize = os.path.getsize(fullpath)
            file_list[fullpath] = filesize
        file_collection["files"] = file_list
    return file_collection

if __name__ == '__main__':
    # argument parsing to allow for adding more, easily
    ap = argparse.ArgumentParser()
    # ap.add_argument("-m", "--mountpoint", default="~", help="mount point to scan")
    ap.add_argument("mountpoint", help="mount point to scan")
    args = vars(ap.parse_args())

    # get the path
    mp = args["mountpoint"]
    json_output = json.dumps(enumeratePaths(mp), indent=4, separators=(',', ': '))
    print json_output
