import os
import shutil
import subprocess
import time

one = "\033[31m"
two = "\033[32m"

extension = ['png', 'jpg', 'svg']

path = "/Users/rosinnovacii/Desktop"
path2 =f"{path}/Delete1"
os.mkdir(path2)

file_name = os.listdir(path)
for m in file_name:
    fileSplit = m.split('.')[-1]
    if fileSplit in extension:
        shutil.move(f"{path}/{m}", f"{path}/Delete/{m}")
        print (one + f"есть такой фаил: {m}")
    else:
        print (two + f"нет такого файла: {m}")

os.rmdir(path2)
