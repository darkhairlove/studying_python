num = int(input())

i = 0
j = 1
k = 0

for h in range(1, num):
    k = i + j
    i = j + k
    j = i + k
print(k, i, j)
