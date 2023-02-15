n, m = map(int, input().split())
st = list(map(int, input().split()))
st = sorted(st)

arr = []


def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    flag = 0
    for i in range(start, n):
        if flag != st[i]:
            arr.append(st[i])
            flag = st[i]
            dfs(i)
            arr.pop()


dfs(0)
