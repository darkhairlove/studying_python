
n, m = map(int, input().split())
st = list(map(int, input().split()))
st = sorted(st)

arr = []


def dfs(idx, cut):
    if cut == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(idx, n):
        idx += 1
        arr.append(st[i])
        dfs(idx, cut+1)
        arr.pop()


dfs(0, 0)
