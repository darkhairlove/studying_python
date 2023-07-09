import sys
import math
input = sys.stdin.readline

N = int(input())
checkpoint = [list(map(int, input().split())) for _ in range(N)]

distance = [0]
for i in range(N - 1):
    dist = abs(checkpoint[i + 1][0] - checkpoint[i][0]) + \
        abs(checkpoint[i + 1][1] - checkpoint[i][1])
    distance.append(dist)

totalDist = sum(distance)
dist = 0
min_dist = math.inf
for i in range(1, N - 1):
    dist = totalDist - (distance[i] + distance[i + 1]) + abs(checkpoint[i + 1]
                                                             [0] - checkpoint[i - 1][0]) + abs(checkpoint[i + 1][1] - checkpoint[i - 1][1])
    min_dist = min(min_dist, dist)
print(min_dist)
