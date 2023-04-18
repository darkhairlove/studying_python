n, M = map(int, input().split())
lesson = list(map(int, input().split()))
l = max(lesson)
r = sum(lesson)
m = (l+r)//2
ans = r


def pos(sz):
    cnt = 1
    blue = 0
    for les in lesson:
        if blue + les <= sz:
            blue += les

        else:
            cnt += 1
            blue = les
    return cnt <= M


while l <= r:
    if pos(m):
        ans = m
        r = m-1
    else:
        l = m+1
    m = (l+r)//2
print(ans)
