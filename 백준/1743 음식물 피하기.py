import sys

sys.setrecursionlimit(10**6)

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M, K = map(int, input().split())
board = [['.']*M for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = '#'

visited = [[False]*M for _ in range(N)]
size = 0
ans = 0


def coord(y, x):
    return 0 <= y < N and 0 <= x < M


def dfs(y, x):
    global size, ans
    visited[y][x] = True
    size += 1
    ans = max(size, ans)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if coord(ny, nx) and not visited[ny][nx] and board[ny][nx] == '#':
            dfs(ny, nx)


for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == '#':
            size = 0

            dfs(i, j)

print(ans)
