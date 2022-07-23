num = int(input())
arr = list()
for i in range(num):
    arr.append(input())

arr.sort()
arr = set(arr)
for i in arr:
    print(i)
