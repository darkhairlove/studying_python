a, b = input().split()

answer = []
for i in range(len(b) - len(a) + 1):
    con = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            con += 1
    answer.append(con)

print(min(answer))
