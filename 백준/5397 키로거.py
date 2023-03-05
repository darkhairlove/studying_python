num = int(input())
for i in range(num):
    st_1 = []
    st_2 = []
    string = input()
    for ch in string:
        if ch == '<':
            if len(st_1):
                st_2.append(st_1.pop())
        elif ch == '>':
            if len(st_2):
                st_1.append(st_2.pop())
        elif ch == '-':
            if len(st_1):
                st_1.pop()
        else:
            st_1.append(ch)
    print("".join(st_1)+''.join(reversed(st_2)))
