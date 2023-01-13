# https://www.acmicpc.net/problem/1620 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    a = input().rstrip()
    dic[i] = a
    dic[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dic[int(quest)])
    else:
        print(dic[quest])

