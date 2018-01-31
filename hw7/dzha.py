def text(name):
    with open ("/Users/Max/Desktop/" + name + ".txt", "r", encoding = "utf-8") as f:
#пишу абсолютные пути, потому что мне так удобнее. haters gonna hate
        return (f.read()).split(" ")

def count(text):
    count = [0,0]
    for word in text:
        if word[-2:] == "ed":
            count[0] += 1
            if word[-3:] == "ied":
                count[1] += 1
    return count

filename = input("Введите имя файла с текстом (без расширения): ")
text = text(filename)
count = count(text)
print("Словоформ на '-ed': ",count[0])
print("Словоформ на '-ied': ",count[1])

#а причем тут словари? 
