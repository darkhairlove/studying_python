def count(n, k):
    cut = 0
    while n:
        n //= k
        cut += n
    return cut


n, k = map(int, input().split())

five = count(n, 5) - count(k, 5) - count(n-k, 5)
two = count(n, 2) - count(k, 2) - count(n-k, 2)
ans = min(five, two)

print(ans)
