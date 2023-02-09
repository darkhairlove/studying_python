
n, m = map(int, input().split())
st = list(map(int, input().split()))
st = sorted(st)

arr = []


def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n):
        arr.append(st[i])
        dfs(i)
        arr.pop()


dfs(0)
