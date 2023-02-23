num = input()
a = int(input())
b = int(num[:-2]+'00')
while True:
    if b % a == 0:
        break
    b += 1
print(str(b)[-2:])
