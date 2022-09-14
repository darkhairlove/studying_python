N, M = map(int, input().split())
A = []
count = []

for _ in range(N):
    A.append(input())

for a in range(N-7):
    for b in range(M-7):
        i_1 = 0
        i_2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if A[i][j] != 'W':
                        i_1 += 1
                    if A[i][j] != 'B':
                        i_2 += 1
                else:
                    if A[i][j] != 'B':
                        i_1 += 1
                    if A[i][j] != 'W':
                        i_2 += 1
        count.append(min(i_1, i_2))

print(min(count))
