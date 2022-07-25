import sys
num = int(sys.stdin.readline())
arr = []
for i in range(num):
    arr.append(sys.stdin.readline().strip())
arr_list = set(arr)
arr = list(arr_list)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
