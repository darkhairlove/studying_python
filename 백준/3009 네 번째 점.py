ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
if ax == bx:
    dx = cx
    if ay != cy:
        dy = ay
    else:
        dy = by
elif ax == cx:
    dx = bx
    if ay != by:
        dy = ay
    else:
        dy = cy
elif cx == bx:
    dx = ax
    if by != ay:
        dy = by
    else:
        dy = cy
print(dx, dy)
