n = int(input("Input N: "))
i = 0
while i < n:
    print('Input a[%(number)d]:'% {"number": i})
    a = input()
    if a == "программирование":
        break
    else:
        print(a)
        i += 1
