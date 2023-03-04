import sys
input = sys.stdin.readline  # 없으면 시간초과

num = int(input())
dic = set() # list로 풀면 시간초과
for i in range(num):
    a, b = input().split()
    if b == 'enter':
        dic.add(a)
    else:
        dic.remove(a)
for i in sorted(dic, reverse=True):
    print(i)
