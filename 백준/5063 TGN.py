# https://www.acmicpc.net/problem/5063
num = int(input())

for _ in range(num):
    r, e, c = map(int, input().split())
    if r < e-c:
        print("advertise")
    elif r > e-c:
        print('do not advertise')
    elif r == e-c:
        print('does not matter')
