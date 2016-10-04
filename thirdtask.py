import os
 
testpath = input('Enter file name: ')
 
if os.path.exists(testpath):
    if os.path.isfile(testpath):
        print('FILE')
    elif os.path.isdir(testpath):
        print('Folder')
        print('objects list: ',os.listdir(testpath))
else:
    print('Does not')
    
    
    
    
#def check_files(file_name,folder="./",name_prefix=None)
