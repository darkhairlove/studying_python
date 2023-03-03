import heapq
import sys
input = sys.stdin.readline  # 없으면 시간초과
num = int(input())
hq = []
for _ in range(num):
    x = int(input())
    if x == 0:
        if len(hq) != 0:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(x), x))  # 앞에 있는 것부터 우선적으로 정렬하므로 튜플로 넣음
