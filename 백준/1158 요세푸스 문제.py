n, k = map(int, input().split())

peo = [i for i in range(1, n+1)]
pt = 0
ans = []
for _ in range(n):
    pt += k - 1
    pt %= len(peo)
    ans.append(peo.pop(pt))

print(f"<{', '.join(map(str, ans))}>")
