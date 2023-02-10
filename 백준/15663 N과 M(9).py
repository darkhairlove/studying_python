# 조금 더 빠름
n, m = map(int, input().split())
st = list(map(int, input().split()))
st = sorted(st)

arr = []
visited = [False] * n


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    flag = 0
    for i in range(n):
        if not visited[i] and flag != st[i]:
            visited[i] = True
            arr.append(st[i])
            flag = st[i]
            dfs()
            visited[i] = False
            arr.pop()


dfs()
# import 해서 푸는 문제
# from itertools import permutations

# N, M = map(int, input().split())
# numlist = list(map(int, input().split()))
# case = sorted(set(permutations(numlist, M)))

# for i in case:
#     for j in i:
#         print(j, end=" ")
#     print()
