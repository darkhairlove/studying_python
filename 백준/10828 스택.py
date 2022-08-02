import sys
num = int(input())
stack = []

for i in range(num):
    sta = sys.stdin.readline().split()
    if sta[0] == 'push':
        stack.append(int(sta[1]))
    elif sta[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif sta[0] == 'size':
        print(len(stack))
    elif sta[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif sta[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
