with open("/Users/Max/Desktop/text.txt", "w", encoding="utf-8") as f:
    word = ":3"
    while word != "":
        word = input("Введите слово: ")
        if word[-2:] == "re" or word[-2:] == "ri" or word[-4:] == "esse" or word[-4:] == "isse" or word[-1:] == "i" or word[-3:] == "iri":
            # учел инфинитивы всех склонений во всех временах. не учел исключения.
            f.write(word)
            f.write("\n")
            print("Записано!")
if not f.writable:
    print("Файл закрыт")
