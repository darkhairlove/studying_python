

def fac(n):
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


n, k = map(int, input().split())

print((fac(n) // (fac(k) * fac(n-k)) % 10007))
