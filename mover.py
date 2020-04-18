import glob
import os
import shutil

file_list=glob.glob(r"C:\\Users\\Owner\\PycharmProjects\\test\\Atcoder\\ABC*.py")
to_path_dir=r"C:\\python_programing\\Atcoder\\ABC"

for filepath in file_list:
    number=filepath.split("\\")[-1][3:6]
    try:
        int(number)
    except ValueError:
        break
    
    try:
        os.mkdir(to_path_dir+number)
    except FileExistsError:
        pass

    shutil.move(filepath, to_path_dir+number+"\\")





