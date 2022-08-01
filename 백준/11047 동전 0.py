
n, m = map(int, input().split())
count = 0
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for coin in arr:
    count += m // coin
    m %= coin
print(count)
