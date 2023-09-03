def fibonacci(n):
    global count2
    f = [1] * (n + 1)
    for i in range(3, n + 1):
        count2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


N = int(input())
count2 = 0

print(fibonacci(N), count2)
