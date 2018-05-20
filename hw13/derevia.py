import os

def search ():
    alldirs = []
    for root, dirs, files in os.walk("."):
        alldirs += dirs
    return alldirs

def getletter (dirs):
    dirs.sort()
    max = 0
    letter = ""
    for dirA in dirs:
        dirA.lower()
        i = 0
        for dirB in dirs:
            dirB.lower()
            if dirA[0] == dirB[0]:
                i += 1
        if max < i:
            max = i
            letter = dirA[0]
    return letter

print ("Большинство названий папок начинаются с буквы ", getletter(search()))
