a, b, c = map(int, input().split())

a %= b
for i in range(c-1):
    a = (a*10) % b

print((a*10)//b)
