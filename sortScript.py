import os
import shutil
import subprocess
import time
from datetime import date, datetime

Red = "\033[31m"
Green = "\033[32m"

extension = ['png', 'jpg', 'svg', 'blend1', 'fbx']

path = "/Users/rosinnovacii/Desktop"
path2 =f"{path}/Delete1"
os.mkdir(path2)

file_name = os.listdir(path)
for m in file_name:
    fileSplit = m.split('.')[-1]
    if fileSplit in extension:
        shutil.move(f"{path}/{m}", f"{path}/Delete1/{m}")
        print (Red + f"есть такой фаил: {m}")
    else:
        print (Green + f"нет такого файла: {m}")

current_date = date.today()
question = input("Хотите удалите все файлы?(y/n):")

if question == "y":
    os.rmdir(path2)
else:
    shutil.move(f"{path}/Delete1", f"{path}/Delete/Delete_{current_date}")
