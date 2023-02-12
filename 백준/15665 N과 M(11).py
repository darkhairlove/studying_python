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
        if flag != st[i]:
            visited[i] = True
            arr.append(st[i])
            flag = st[i]
            dfs()
            visited[i] = False
            arr.pop()


dfs()
