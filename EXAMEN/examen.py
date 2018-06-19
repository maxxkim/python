import re
import collections

def readfile (name):
    text = ""
    for i in name:
        with open(i+".xhtml", "r", encoding='windows-1251') as f:
            text += f.read()
    return text

def makecsv (text):
    text = text.split("\n")
    with open("krout.txt", "w", encoding="utf-8") as f:
        f.write ("doc_id\ttitle\tauthor\tcreated\ttopic\ttagging\n")
        f.write (name)
        f.write ("\t")
        for i in text:
            if "title" in i:
                f.write (i[7:-8])
                f.write("\t")
            if "author" in i:
                tmp = i.split(" ")
                f.write (tmp[1][9:])
                f.write (" ")
                f.write (tmp[2][:-1])
                f.write ("\t")
            if "tagging" in i:
                tmp = i.split(" ")
                f.write (tmp[1][9:-1])
                f.write("\t")
            if "created" in i:
                tmp = i.split(" ")
                f.write (tmp[1][9:-1])
                f.write ("\t")
            if "topic" in i:
                tmp = i.split(" ")
                f.write (tmp[1][9:-1])
                f.write("\t")
                f.write("\n")

#_itartass1

def countabb (text):
    abb = re.findall("lex=\"[А-Я][А-Я\-]+",text)
    abb = collections.Counter(abb)
    with open("krout2.txt", "w", encoding="utf-8") as f:
        for key,value in abb.items():
            f.write (key[5:])
            f.write ("\t")
            f.write(str(value))
            f.write ("\n")
    if not f.writable:
        print("Файл недоступен")

print("Задание 1")
namelist = []
name = " "
while  name != "":
    name = input("Введите имя файла (или пустую строку): ")
    if name != "":
        namelist.append(name)
makecsv(readfile(namelist))
print("Выполнено!\nВыходной файл: krout.txt")
print("Задание 2")
countabb(readfile(namelist))
print("Выполнено!\nВыходной файл: krout2.txt")
