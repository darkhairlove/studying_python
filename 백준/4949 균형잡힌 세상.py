
while 1:
    s = input()
    if s == '.':
        break
    arr = []
    flag = True
    for i in s:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] == '[':
                flag = False
                break
            elif arr[-1] == '(':
                arr.pop()
        elif i == ']':
            if not arr or arr[-1] == '(':
                flag = False
                break
            elif arr[-1] == '[':
                arr.pop()
    if flag == True and not arr:
        print("yes")
    else:
        print("no")
