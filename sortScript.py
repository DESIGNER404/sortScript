import os
import shutil
import subprocess
import time
from datetime import date, datetime

one = "\033[31m"
two = "\033[32m"

extension = ['png', 'jpg', 'svg', 'blend1']

path = "/Users/rosinnovacii/Desktop"
path2 =f"{path}/Delete1"
os.mkdir(path2)

file_name = os.listdir(path)
for m in file_name:
    fileSplit = m.split('.')[-1]
    if fileSplit in extension:
        shutil.move(f"{path}/{m}", f"{path}/Delete1/{m}")
        print (one + f"есть такой фаил: {m}")
    else:
        print (two + f"нет такого файла: {m}")


question = input('Хотите удалите все файлы?(Y/N): ')

if question == "Y":
    os.rmdir(path2)
else:
    current_date = date.today()
    shutil.move(f"{path}/Delete1", f"{path}/Delete/Delete_{current_date}")
