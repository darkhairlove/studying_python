a = int(input())
i = 8
j = 1
while 1:
    if i-6*j <= a % i <= i-1 and a // i == 0:
        print(j+1)
        break
    elif a == 1:
        print("1")
        break
    else:
        j += 1
        i += 6*j
