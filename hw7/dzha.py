def text():
    with open ("/Users/Max/Desktop/text.txt", "r", encoding = "utf-8") as f:
#пишу абсолютные пути, потому что мне так удобнее. haters gonna hate 
        return (f.read()).split(" ")

text = text()
count_ed = 0
count_ied = 0
for word in text:
    if word[-2:] == "ed":
        count_ed += 1
        if word[-3:] == "ied":
            count_ied += 1
print("Словоформ на '-ed': ",count_ed)
print("Словоформ на '-ied': ",count_ied)

#а причем тут словари? 
