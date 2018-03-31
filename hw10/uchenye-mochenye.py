import re

name = input("Введите название html файла статьи: ")
resultfilename = input("Введите название выходного файла: ")

with open(name + ".html", "r", encoding="utf-8") as file:
    text = file.read()

text = text.split("\n")

flag = 0

for line in text:
    if flag != 0:
        a = line
        break
    if re.search("Научная сфера",line):
        flag = 1

res = re.findall("[а-я]+",line, flags=re.IGNORECASE)

i = 0
for word in res:
    if re.search("[А-Я]+",word):
        res.pop(i)
    i += 1


with open(resultfilename + ".txt", "w", encoding="utf-8") as f:
    f.write(str(res))
if not f.writable:
    print("Файл закрыт")
