f = open("/Users/Max/Desktop/text.txt", encoding="utf-8")
text = f.read()
f.close()
text = text.split(" ")
c1 = 0
c2 = 0
for word in text:
    n = len(word)-1
    if word[n] == ".":
        c1 += 1
    elif word[n] == ",":
        c1 += 1
    else:
        c2 += 1
res = c1/(c2+c1)*100
print("Процент слов, заканчивающихся точкой или запятой =", res, "%")
