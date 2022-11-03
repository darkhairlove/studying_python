n = int(input())
arr = []
arr2 = []
for _ in range(n):
    arr.append(input())
for x in arr:
    if x not in arr2:
        arr2.append(x)
        
con = [arr.count(x) for x in arr2]
ind = []

for i in range(len(con)):
    if con[i] == max(con):
        ind.append(i)
print(sorted([arr2[i] for i in ind])[0])
        