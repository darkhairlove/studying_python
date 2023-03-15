rat = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            rat[i][j] = 1

anw = 0

for row in rat:
    anw += sum(row)
print(anw)
