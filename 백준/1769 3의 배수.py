import sys

word = list(map(int, sys.stdin.readline().strip()))
cnt = 0
while len(word) > 1:
    cnt += 1
    temp = []
    word = sum(word)
    for i in str(word):
        temp.append(int(i))

    word = temp
print(cnt)

if word[0] % 3 == 0:
    print("YES")
else:
    print("NO")
