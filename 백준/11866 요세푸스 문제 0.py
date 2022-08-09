from collections import deque
n, m = map(int, input().split())
que = deque()
for i in range(1, n+1):
    que.append(i)
print("<", end="")
while que:
    for i in range(m-1):
        que.append(que[0])
        que.popleft()
    print(que.popleft(), end="")
    if que:
        print(', ', end="")
print(">")
