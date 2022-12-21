a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_soce = list()
b_soce = list()
con = list()
for i, j in zip(a, b):
    if i == j:
        a_soce.append(1)
        b_soce.append(1)
        con.append('D')
    elif i > j:
        a_soce.append(3)
        b_soce.append(0)
        con.append('A')
    elif i < j:
        a_soce.append(0)
        b_soce.append(3)
        con.append('B')
if sum(a_soce) > sum(b_soce):
    a = 'A'
elif sum(a_soce) < sum(b_soce):
    a = 'B'
else:
    if 'B' and 'A' in con:
        for i in range(len(con)-1, 0, -1):
            if con[i] == 'D':
                continue
            else:
                a = con[i]
                break
    else:
        a = 'D'


print(sum(a_soce), sum(b_soce))
print(a)
