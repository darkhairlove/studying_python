num, l, P = map(int, input().split())

c = list(map(int, input().split()))
d = list(map(int, input().split()))

c.sort()
d.sort()
con = 0
for i in d:
    if i in c:
        d.remove(i)
        c.remove(i)

for i in c:
    if i-1 in d:
        d.remove(i-1)

    if i+1 in d:
        d.remove(i+1)
    else:
        con += 1
print(con)

n, s, r = map(int, input().split())
t = [0 for i in range(n)]
b_t = [*map(int, input().split())]
s_t = [*map(int, input().split())]

for i in s_t:
    if i in b_t:
        del b_t[b_t.index(i)]
        continue
    t[i-1] += 1
for i in b_t:
    if i == n:
        if t[i-2] == 1:
            t[i-2] -= 1
            continue
        else:
            t[i-1] -= 1
    elif i == 1:
        if t[i] == 1:
            t[i] -= 1
            continue
        else:
            t[i-1] -= 1
    elif i < n:
        if t[i-2] == 1:
            t[i-2] -= 1
            continue
        elif t[i] == 1:
            t[i] -= 1
            continue
        else:
            t[i-1] -= 1

print(t.count(-1))
