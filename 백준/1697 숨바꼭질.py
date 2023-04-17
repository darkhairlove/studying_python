from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 10**5 and not dist[nx]:
                dist[nx] = dist[x]+1
                q.append(nx)
                print(nx)
                print(dist[nx])


dist = [0]*(10**5+1)
n, k = map(int, input().split())
bfs()
