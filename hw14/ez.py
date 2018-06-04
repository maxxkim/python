import re

def readfile ():
    with open("ozhegov.txt", "r", encoding='utf-8') as f:
        text = f.read()
        return text

def killpunctuation (text):
    text = re.sub(u"[^а-яА-Я0-9!?. \\n]", "", text)
    text = re.sub(u"[!?.]", "Ə", text)
    return text

def makedic(text):
    text = text.split("Ə")
    dic = {sent: sent.split() for sent in text}
    for key, value in dic.items():
        dic[key] = {word: len(word) for word in key.split()}
    return dic

print (makedic(killpunctuation(readfile())))
