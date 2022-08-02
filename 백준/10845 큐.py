import sys
from collections import deque
num = int(input())
queue = deque([])

for i in range(num):
    que = sys.stdin.readline().split()
    if que[0] == 'push':
        queue.append(int(que[1]))
    elif que[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif que[0] == 'size':
        print(len(queue))
    elif que[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif que[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif que[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
