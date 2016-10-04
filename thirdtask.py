
import os
a = u'/home/katya/Myprojects/Tests'
def check_files(file_names,folder="/",name_prefix=None):
    for name in file_names:
        if os.path.exists(a+folder+name):
            print ("Exists")
        else:
            print ("Does not")
check_files(["thirdtask.py", "firsttask.py"])

