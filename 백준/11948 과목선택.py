lis = list()
lis1 = list()
for i in range(4):
    lis.append(int(input()))
for i in range(2):
    lis1.append(int(input()))
sorted(lis)
sorted(lis1)
print(sum(lis[-3:]) + lis1[1])
