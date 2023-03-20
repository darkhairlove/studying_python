n, m = map(int, input().split())

buk = [i for i in range(1, n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    buk = buk[:i] + buk[k:j+1] + buk[i:k] + buk[j+1:]
print(*buk)
