import os
import random

def check_files(seek_file_names, folder="./", name_prefix=None, n=7):
    for name in seek_file_names:
        a = os.path.join(folder, name)
        if os.path.exists(a):
            print ("Exists")
        else:
            print_lines(name)

def print_lines(name, n=7):
    with open (name, 'w') as f:
        i = 0
        while i < n:
            t = random.randint(4, 590)
            t = str(t)
            f.write(t + '\n')
            i = i + 1
    f.closed

if __name__ == "__main__":
    check_files(["thirdtask.py", "firsttask.py", "zuat"])


