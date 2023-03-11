import sys
input = sys.stdin.readline
meet = []

for _ in range(int(input())):
    start, end = map(int, input().split())
    meet.append((end, start))

meet.sort()
t = 0
ans = 0
for end, start in meet:
    if t <= start:
        ans += 1
        t = end
print(ans)
