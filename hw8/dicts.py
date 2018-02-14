import random

def readfile(name):
    with open (name + ".txt", "r", encoding = "utf-8") as f:
        return random.choice((f.read()).split("\n"))

def makedic(line):
    line = line.split(" ")
    line = {line[0]: line[1]}
    return (line)

filename = input("Введите имя файла с данными (без расширения): ")
hints = readfile(filename)
hints = makedic(hints)
j = 0
print( list( hints.values())[0], end = " ")
while j < len (list(hints.values())[0]):
    print (".",end = "")
    j += 1
print("\n")
word = input("Попробуйте угадать слово за многоточием: ")
while word not in hints.keys():
    word = input("Попробуйте еще раз: ")
print("Поздравляю, вы угадали!")
