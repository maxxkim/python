import re

def readfile(name):
    with open(name, "r", encoding="utf-8") as f:
        text = f.read()
        return text

def writefile(text,name):
    with open(name, "w", encoding="utf-8") as f:
        f.write(text)
    if not f.writable:
        print("Unable to get access to the end file.")

def substitute(text):
    text = re.sub('философия', 'астрология', text)
    text = re.sub('Философия', 'Астрология', text)
    text = re.sub('философии', 'астрологии', text)
    text = re.sub('Философии', 'Астрологии', text)
    text = re.sub('философией', 'астрологией', text)
    text = re.sub('Философией', 'Астрологией', text)
    text = re.sub('философий', 'астрологий', text)
    text = re.sub('Философий', 'Астрологий', text)
    text = re.sub('философию', 'астрологию', text)
    text = re.sub('Философию', 'Астрологию', text)
    text = re.sub('философиями', 'астрологиями', text)
    text = re.sub('Философиями', 'Астрологиями', text)
    text = re.sub('философиях', 'астрологиях', text)
    text = re.sub('Философиях', 'Астрологиях', text)
    return text

writefile(substitute(readfile(input("Enter in file name: "))), input ("Enter out file name: "))
