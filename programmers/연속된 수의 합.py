def solution(num, total):
    if num % 2 == 0:
        start = total//num-(num//2-1)
        ans = list(range(start, start+num))
    else:
        start = total//num - num//2
        ans = list(range(start, start+num))
    return ans
