import re

def readfile():
    with open("/Users/Max/Desktop/f.xml", "r", encoding="utf-8") as f:
        text = f.read()
        return text

def fun1(a):
    with open("/Users/Max/Desktop/corpusout.txt", "a", encoding="utf-8") as f:
        f.write("–Задание 1–\n")
        a = a.split("\n")
        f.write(str(len(a))+"\n")
    if not f.writable:
        print("Unable to get access to the end file.")

def fun2(b):
    with open("/Users/Max/Desktop/corpusout.txt", "a", encoding="utf-8") as f:
        f.write("–Задание 2–\n")
        masterdict = {}
        b = b.split("\n")
        c = 0
        for line1 in b:
            if line1.find("<w lemma=") != -1:
                line1 = line1.split(" ")
                j = 0
                for line2 in b:
                    if line2.find("<w lemma=") != -1:
                        line2 = line2.split(" ")
                        if line1[14] == line2[14]:
                            c += 1
                            b.pop(j)
                j += 1
                dict = {line1[14] : c}
                masterdict.update(dict)
                c = 0
        for key in masterdict:
            f.write (key)
            f.write("\n")
    if not f.writable:
        print("Unable to get access to the end file.")

def fun3(c):
    with open("/Users/Max/Desktop/courpusout.txt", "a", encoding="utf-8") as f:
        f.write("–Задание 3–\n")
        c = c.split("\n")
        i = 0
        for line1 in c:
            if line1.find("<w lemma=") != -1 and re.search("l[a-z]f[a-z]+",line1):
                line1 = line1.split(" ")
                j = 0
                i = 0
                for line2 in c:
                    if line2.find("<w lemma=") != -1 and re.search("l[a-z]f[a-z]+",line2):
                        line2 = line2.split(" ")
                        if line1[14] == line2[14]:
                            i += 1
                            c.pop(j)
                    j += 1
                f.write(line1[14])
                f.write(" ")
                f.write(str(i))
                f.write("\n")
    if not f.writable:
        print("Unable to get access to the end file.")

def funadd(d):
    with open("/Users/Max/Desktop/corpusout.csv", "w", encoding="utf-8") as f:
        f.write("–Задание 3–\n")
        d = d.split("<body>")
        d = d[1].split("</body>")
        d = d[0]
        d = re.sub('<[a-z]+>', '', d, re.IGNORECASE)
        d = re.sub('</[a-z]+>', '', d, re.IGNORECASE)
        d = re.sub('<[a-z] ', '', d)
        d = re.sub('/>', '', d)
        d = re.sub('/[a-z]>', '', d)
        d = re.sub('[a-z]+=', '', d)
        d = d.split("\n")
        for line in d[3:-4]:
            line = line.split(" ")
            for word in line:
                if word != "":
                    f.write(word)
                    f.write(", ")
            f.write("\n")
    if not f.writable:
        print("Unable to get access to the end file.")

fun1(readfile())
fun2(readfile())
fun3(readfile())
funadd(readfile())
