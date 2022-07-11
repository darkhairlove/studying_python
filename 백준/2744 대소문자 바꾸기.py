
arr = input()
ans = list()
for i in arr:
    if 91 > ord(i) and ord(i) > 64:
        ans.append(chr(ord(i)+32))
    elif 123 > ord(i) and ord(i) > 96:
        ans.append(chr(ord(i)-32))
print(''.join(ans))
