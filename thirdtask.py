"""
We have the list like ["Marun-001-002", "Merin 002-002", etc].
Create a function (check_files(seek_file_names, folder="./", name_prefix=None))to check if the file exists
in the directory. Name_prefix is not required. If it is defined, we are into only the names,
that start with this prefix.
"""

# -*- coding: utf-8 -*-
import os
def check_files(seek_file_names, folder="./", name_prefix=None):
    """
    :param seek_file_names: the list with potential file names
    :param folder: wanted folder for seeking the file
    """
    for name in seek_file_names:
        a = os.path.join(folder, name)
        if os.path.exists(a):
            print ("Exists")
        else:
            print ("This file does not exist")

if __name__ == "__main__":
    check_files(["thirdtask.py", "firsttask.py", "hhhh"])

