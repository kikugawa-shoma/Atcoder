import os
import sys 

root_path = r"C:\Users\ktmks\programming\kyopro\Atcoder\ABC\ABC"

#if len(sys.argv) != 2:

os.makedirs(root_path + sys.argv[1],exist_ok=True)

filename = "A"

for i in range(6):
    path = root_path + sys.argv[1] + "\\" + filename + ".py"
    if not os.path.exists(path):
        f = open(path,mode="w")
        f.close()
    
    path = root_path + sys.argv[1] + "\\" + filename + ".cpp"
    if not os.path.exists(path):
        f = open(path,mode="w")
        f.close()
    filename = chr(ord(filename) + 1)
