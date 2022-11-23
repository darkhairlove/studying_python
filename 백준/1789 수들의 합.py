import sys
num = int(sys.stdin.readline())
plus = 0
cnt = 0
for i in range(1, num+1):
    plus += i
    cnt += 1
    if plus > num:
        cnt -= 1
        break
print(cnt)
