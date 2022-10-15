import sys

input = sys.stdin.readline

num, new, p = map(int, input().split())
if num:
    score = list(map(int, input().split()))
    score.append(new)
    score.sort(reverse=True)
    i = score.index(new)+1
    if i > p:
        print(-1)
    else:
        if num == p and new == score[-1]:
            print(-1)
        else:
            print(i)
else:
    print(1)
