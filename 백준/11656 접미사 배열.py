
S = input()

suffix = []
for i in range(len(S)):
    suffix.append(S[i:])

suffix.sort()
for i in suffix:
    print(i)
