with open("/Users/Max/Downloads/quotes.txt", "r", encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
    print("--Задание 1--\n")
    for line in text:
        quote = line.split("—")
        words = quote[0].split(" ")
        if len(words) <= 9 and len(words[0]) < 5:
            print(quote[0], "–", quote[1])
    print("\n--Задание 2--\n")
    i = 0
    for line in text:
        quote = line.split("—")
        #спросил у преподавателя, разрешила искать только вхождения с . , ? и !
        if "разум " in quote[0] or "разум." in quote[0] or "разум," in quote[0] or "разум!" in quote[0] or "разум?" in quote[0]:
            i += 1
            print(quote[0])
    print("\nФраз с вхождением слова 'разум' –", i)
    print("\n--Задание 3--\n")
    wordlist = []
    stream = "-"
    while stream != "":
        stream = input("Введите слово: ")
        wordlist.append(stream)
    for entry in wordlist[:-1]:
        flag = 0
        print("\n", entry, ": \n")
        for line in text:
            quote = line.split("—")
            if entry in quote[0]:
                flag = 1
                print(quote[1], "\t", quote[0])
        if flag == 0:
                print("Вхождения слова", entry, "не было")
