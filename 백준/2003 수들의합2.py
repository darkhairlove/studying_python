N, M = map(int, input().split())
num = list(map(int, input().split()))

lef, rig = 0, 1
con = 0

while rig <= N and lef <= rig:
    sum_num = num[lef:rig]
    total = sum(sum_num)

    if total == M:
        con += 1
        rig += 1
    elif total < M:
        rig += 1
    else:
        lef += 1
print(con)
