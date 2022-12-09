def solution(nl, n):
    ans = []
    nl.sort()
    if n < max(nl):
        a = max(nl)
    else:
        a = n
    for i in range(a, -1, -1):
        for j in nl:
            if n - j >= 0 and n-j == i:
                ans.append(j)
            elif n - j < 0 and abs(n-j) == i:
                ans.append(j)
    ans.reverse()

    return ans
