def solution(s):
    for i in range(len(s)//2):
        j = len(s)-i-1
        if s[i] != s[j]:
            return -1
    return 1


print(solution("asvd"))
print(solution("assa"))
print(solution("a"))
