num = int(input())
a, b = map(int, input().split())
cnt = a//2 + b

if cnt > num:
    print(num)
else:
    print(cnt)
