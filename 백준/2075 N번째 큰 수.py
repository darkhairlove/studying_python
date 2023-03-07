import heapq
num = int(input())

hp = []

for _ in range(num):
    s = map(int, input().split())
    for i in s:
        if len(hp) >= num:
            heapq.heappushpop(hp, i)
            print(hp)
        else:
            heapq.heappush(hp, i)
            print(hp)
print(heapq.heappop(hp))
