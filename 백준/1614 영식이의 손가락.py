import sys
fig = int(sys.stdin.readline())
Rep = int(sys.stdin.readline())
answer = 0
# if 1 or 5
if fig == 1:
    if Rep == 0:
        answer += fig-1
    else:
        answer += 8*Rep
elif fig == 5:
    if Rep == 0:
        answer += fig-1
    else:
        answer += 4 + 8*(Rep)
# else 2,3,4
else:
    if Rep == 0:
        answer += fig-1
    else:
        answer += 4*(Rep) + 1
        if Rep % 2 == 0:
            answer += fig-2
        else:
            answer += 4-fig
print(answer)
