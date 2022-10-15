

n, m = map(int, input().split())
p = []

for i in range(m):
    p.append(int(input()))

p = sorted(p, reverse=True)

price = 0
max = 0

for i in range(m):
    if i + 1 > n:
        profit = p[i]*n
    else:
        profit = p[i]*(i+1)
    if max < profit:
        price = p[i]
        max = profit
print(price, max)
