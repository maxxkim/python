b = input("Введите слово: ")
n = len(b)
a = []
i = 0
while i < n:
    a.append(b[i])
    i+=1
i = 0
while i < n:
    print(str(a))
    j = n-1
    temp = a[j]
    while j > 0:
        a[j] = a[j-1]
        j-=1
    a[0] = temp
    i+=1
 
