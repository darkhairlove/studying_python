def chain_(arr, num):

    chain_count = num
    chain = 1
    for i in arr:
        if chain + i >= chain_count:
            break
        else:
            chain += i

            chain_count -= 1
    print(chain_count-1)


num = int(input())
arr = list(map(int, input().split()))
arr.sort()
chain_(arr, num)
