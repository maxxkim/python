import re
import os
def proga():
    return re.findall("[a-z]+\.[a-z]+", str(os.listdir()), flags = re.IGNORECASE)
print(proga(),"\n",len(proga())) #первый раз залил до дедлайна, просто хотел, чтобы прога была в 5 строк
