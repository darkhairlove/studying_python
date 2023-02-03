num = int(input())
a = 0
b = 0
c = 0
if num > 300 and num % 300 != 0:
    while 1:
        num -= 300
        a += 1
        if num < 300:
            break
elif num >= 300 and num % 300 == 0:
    a += (num // 300)
    num -= (num // 300) * 300

if num > 60 and num % 60 != 0:
    while 1:
        num -= 60
        b += 1
        if num < 60:
            break
elif num >= 60 and num % 60 == 0:
    b += (num // 60)
    num -= (num // 60) * 60

if num > 10 and num % 10 != 0:
    while 1:
        num -= 10
        c += 1
        if num < 10:
            break
elif num >= 10 and num % 10 == 0:
    c += (num // 10)
    num -= (num // 10) * 10
if num % 10 != 0:
    print(-1)
else:
    print(a, b, c)
