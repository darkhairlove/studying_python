import sys
input = sys.stdin.readline
num = int(input())
dic = {}
for i in range(num):
    a = int(input())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
arr = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(arr[0][0])
