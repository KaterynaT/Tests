import os
import random


def check_files(seek_file_names, folder="./", name_prefix=None):
    for name in seek_file_names:
        a = os.path.join(folder, name)
        if os.path.exists(a):
            print ("Exists")
        else:
            print_lines(name)


def print_lines(name, n=7):
    with open(name, 'w') as f:
        for i in range (0, n):
            t = str(random.randint(0, 1000))
            f.write(t + '\n')

if __name__ == "__main__":
    check_files(["thirdtask.py", "firsttask.py", "Suat"])


