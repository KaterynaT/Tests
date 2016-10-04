import os
import random
def check_files(seek_file_names, folder="./", name_prefix=None,N=7):
    for name in seek_file_names:
        a = os.path.join(folder, name)
        if os.path.exists(a):
            print ("Exists")
        else:
            f = open(name, 'w')
            i = 0
            while i<=N:
                t = random.randint(4, 590)
                t = str(t)
                f.write(t +'\n')
                i = i+1

if __name__ == "__main__":
    check_files(["thirdtask.py", "firsttask.py", "qq"])

