n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(input())
for _ in range(m):
    arr2.append(input())
con = 0
for i in arr2:
    if i in arr1:
        con += 1
print(con)
