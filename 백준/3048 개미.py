import sys
n1, n2 = map(int, sys.stdin.readline().split())

an1 = list(map(str, sys.stdin.readline().rstrip("\n")))
an2 = list(map(str, sys.stdin.readline().rstrip("\n")))
t = int(sys.stdin.readline())
an1.reverse()
an = an1+an2
for _ in range(t):
    for i in range(len(an) - 1):
        if an[i] in an1 and an[i + 1] in an2:
            an[i], an[i + 1] = an[i + 1], an[i]

            if an[i + 1] == an1[-1]:
                break

print("".join(an))
