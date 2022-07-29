num = int(input())
line = input()
answer = 0
for i in range(num):
    answer += (ord(line[i])-96) * (31 ** i)
print(answer % 1234567891)
