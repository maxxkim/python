import re

filename = input('Input file name: ')
resultfilename = input('Input result file name: ')
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()
with open(resultfilename, "w", encoding="utf-8") as f:
    f.write(str(re.findall("вып[е]...[^а-я]", text)))
    f.write(str(re.findall("вып[ьи]..[^а-я]", text)))
    f.write(str(re.findall("вып[еьи].[^а-я]", text)))
if not f.writable:
    print("File is closed")

#я чорт знает почему он выводит \n в текстовик, чинить это смысла нет имхо
