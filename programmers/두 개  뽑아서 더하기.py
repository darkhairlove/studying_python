# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(num):
    ans = {}
    for i in range(len(num)):
        a = num[i]
        for k in range(i+1, len(num)):
            ans[a+num[k]] = i
    ans = list(ans.keys())
    ans.sort()
    return ans
