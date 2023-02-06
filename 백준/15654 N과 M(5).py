
n, m = map(int, input().split())
st = list(map(int, input().split()))
st = sorted(st)

arr = []


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in st:
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()


dfs()
