num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    a = int('0b'+str(a), 2)
    b = int('0b'+str(b), 2)
    c = a+b
    c = bin(c)
    print(c[2:])
