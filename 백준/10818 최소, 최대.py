
N = int(input())
c = list(map(int, input().split()))

i = 1
j = 1
ma = -1000000
mi = 1000000
for i in c:
    if i > ma:
        ma = i
for j in c:
    if j < mi:
        mi = j
print(mi, ma)
