import re

def readfile ():
    with open("ozhegov.txt", "r", encoding='utf-8') as f:
        text = f.read()
        return text

def killpunctuation (text):
    cleartext = re.sub(u"[^а-яА-Я0-9 \\n]", "", text)
    return cleartext

def makedic(text):
    text = text.split()
    dic = {i: len(i) for i in text}
    return dic

print (makedic(killpunctuation(readfile())))
