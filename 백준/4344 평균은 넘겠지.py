ans = int(input())
an = 0
arr = 0
for i in range(ans):
    num = list(map(int, input().split()))
    arr = (sum(num) - num[0]) // num[0]
    for i in range(1, len(num)):
        if num[i] > arr:
            an += 1
    print("{:.3f}%".format((100*an)/num[0]))
    arr = 0
    an = 0
