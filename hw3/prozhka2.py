a=input("Введите слово: ")
if a != "":
 for letter in a:
     print(a)
     a=a[-1]+a[:-1]
