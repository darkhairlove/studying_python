import sys
input =sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    swp = input().strip().split()
    
    if len(swp) == 1:
        if swp[0]=='all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
            
    else:
        fn, x = swp[0], swp[1]
        x = int(x)
        if fn =='add':
            s.add(x)
        elif fn == 'remove':
            s.discard(x)
        elif fn == 'check':
            print(1 if x in s else 0)
        elif fn == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
                           