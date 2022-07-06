H, M = map(int, input().split())

if(44 < M <= 59):
    print(H, M-45)
else:
    if(H == 0):
        print(23, M+60-45)
    else:
        print(H-1, M+60-45)
