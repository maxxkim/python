import re
import os

def proga():
    file_list = os.listdir()
    file_list = re.findall("[a-z]+\.[a-z]+", str(file_list), flags = re.IGNORECASE)
    return file_list

print(proga())
print(len(proga()))
