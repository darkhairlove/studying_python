
num = 1000 - int(input())

count = 0
arr = [500, 100, 50, 10, 5, 1]

for coin in arr:
    count += num // coin
    num %= coin
print(count)
