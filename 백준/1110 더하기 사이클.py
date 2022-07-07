N = int(input())
i = 0
answer = N
while True:
    A = N // 10
    B = N % 10
    n = A + B
    N = B*10 + n % 10
    if answer == N:
        print(i+1)
        break
    else:
        i += 1
        continue
