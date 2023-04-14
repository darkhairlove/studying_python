num = int(input())

cached = [0]*(num+1)


def dp(num):
    if cached[num]:
        return cached[num]
    if num <= 2:
        cached[num] = num
    else:
        cached[num] = (dp(num-1)+dp(num-2)) % 10007
    return cached[num]


print(dp(num))
