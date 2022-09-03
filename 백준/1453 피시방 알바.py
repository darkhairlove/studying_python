n = int(input())
lis = list(map(int, input().split()))
pc = [0] * 101
cut = 0
for i in lis:
    if pc[i] != 0:
        cut += 1
    else:
        pc[i] += 1
print(cut)
