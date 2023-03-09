num = int(input())
T = []

for n in range(46):
    T.append(n*(n+1)//2)


def pos(K):

    for i in range(1, 46):
        for j in range(i, 46):
            for k in range(j, 46):
                if T[i]+T[j]+T[k] == K:
                    return(1)
    else:
        return(0)


for _ in range(num):
    print(pos(int(input())))
