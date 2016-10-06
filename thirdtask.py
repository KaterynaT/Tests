"""
We have the list like ["Marun-001-002", "Merin 002-002", etc].
Create a function (check_files(seek_file_names, folder="./", name_prefix=None))to check if the file exists
in the directory. Name_prefix is not required. If it is defined, we are into only the names,
that start with this prefix.
"""

# -*- coding: utf-8 -*-
import os

def check_files(seek_file_names, folder="./", name_prefix=None):
    # type: (object, object, object) -> object
    """
    :param seek_file_names: the list with potential file names
    :param folder: wanted folder for seeking the file
    """
    list = []
    list2 = []
    for name in seek_file_names:
        a = os.path.join(folder, name)
        if os.path.exists(a):
            list.append(a)
        else:
            list2.append(a)
    print list
    return list

if __name__ == "__main__":
    check_files(["thirdtask.py","ttttt","ppopopo"])

