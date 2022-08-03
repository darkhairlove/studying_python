N = int(input())
num = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
num.sort()

for i in numbers:
    lt, rt = 0, N-1
    isExist = False

    while lt <= rt:
        mid = (lt + rt)//2
        if i == num[mid]:
            isExist = True
            print(1)
            break
        elif i > num[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    if not isExist:
        print(0)
