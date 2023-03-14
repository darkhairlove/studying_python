from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]
chk = [[False] * M for _ in range(N)]
dp = deque()
dp.append((0, 0, 1))
chk[0][0] = True


def coord(y, x):
    return 0 <= y < N and 0 <= x < M


while len(dp) > 0:
    y, x, d = dp.popleft()

    if y == N-1 and x == M-1:
        print(d)
        break
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        nd = d+1
        if coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
            chk[ny][nx] = True
            dp.append((ny, nx, nd))
