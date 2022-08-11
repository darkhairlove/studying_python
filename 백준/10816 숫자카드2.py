import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
num.sort()
arr = []
numberdic = {}
for a in num:
    if a not in numberdic:
        numberdic[a] = 1
    else:
        numberdic[a] += 1

for i in numbers:
    lt, rt = 0, N-1
    while lt <= rt:
        mid = (lt + rt)//2
        if i == num[mid]:
            break
        elif i > num[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    if num[mid] == i:
        print(numberdic[i], end=" ")
    else:
        print(0, end=" ")
