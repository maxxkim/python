import random

#в японском языке "н" - тоже слог (нагуглил)
#файлы noun1, verb 3,... в папке hw6 вместе с этим файлом
#путь к нужному файлу в функциях осуществляется с помощью конкатенации строк. 

#возвращает существительное (или имя собств.) длины a
def noun(a):
    a = "/Users/Max/Desktop/noun" + str(a) + ".txt"
    with open(a, "r", encoding='utf-8') as f:
        nouns = f.read()
        nouns = nouns.split("\n")
        return random.choice(nouns)
#возвращает глагол в настоящем или будущем (в яп. яз. совпадают) времени длины a
def verbpr(a):
    a = "/Users/Max/Desktop/verb" + str(a) + ".txt"
    with open(a, "r", encoding='utf-8') as f:
        nouns = f.read()
        nouns = nouns.split("\n")
        return random.choice(nouns)
#возвращает глагол в прошедшем времени длины a
def verbpst(a):
    a = "/Users/Max/Desktop/verb" + str(a) + " 2.txt"
    with open(a, "r", encoding='utf-8') as f:
        nouns = f.read()
        nouns = nouns.split("\n")
        return random.choice(nouns)
#возвращает указатель на момент времени или временной отрезок (фиксированная длина)
def time():
    with open("/Users/Max/Desktop/time.txt", "r", encoding='utf-8') as f:
        nouns = f.read()
        nouns = nouns.split("\n")
        return random.choice(nouns)

#служебные слова (падежные показатели итд. ставлю сам, остальное через функции)
def random_haiku():
    tense = random.random()
    if tense > 0.5:
        sentype = random.random()
        if sentype > 0.5:
            verblen = random.randint(2,3)
            addlen = 4 - verblen
            haiku = time() + "まで\n"+ noun(6) + "は\n"+ noun(addlen) + "を" + verbpr(verblen)
        else:
            objlen = random.randint(1,4)
            addlen = 6 - objlen
            haiku = time() + "まで\n" + noun(objlen) + "は" + noun(addlen) + "を\n" + verbpr(5)
    else:
        sentype = random.random()
        if sentype > 0.5:
            verblen = random.randint(2,3)
            addlen = 4 - verblen
            haiku = time() + "から\n"+ noun(6) + "は\n"+ noun(addlen) + "を" + verbpst(verblen)
        else:
            objlen = random.randint(1,4)
            addlen = 6 - objlen
            haiku = time() + "から\n" + noun(objlen) + "は" + noun(addlen) + "を\n" + verbpst(5)
    return haiku

print(random_haiku())
