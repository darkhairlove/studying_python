def solution(quiz):
    ans = []
    for i in quiz:
        a = i.split(' ')
        if a[1] == '-':
            if int(a[4]) == int(a[0])-int(a[2]):
                ans.append("O")
            else:
                ans.append("X")
        else:
            if int(a[4]) == int(a[0])+int(a[2]):
                ans.append("O")
            else:
                ans.append("X")
    return ans
# 다른 풀이


def solution(quiz):
    ans = []
    for i in quiz:
        a = i.split(' ')
        if a[1] == '-':
            if int(a[4]) == int(a[0])-int(a[2]):
                ans.append("O")
                continue
        else:
            if int(a[4]) == int(a[0])+int(a[2]):
                ans.append("O")
                continue
        ans.append("X")
    return ans
