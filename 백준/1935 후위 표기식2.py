num = int(input())
num_val = []
stk = []
string = input()
for _ in range(num):
    num_val.append(int(input()))

for ch in string:
    if ch.isalpha():
        stk.append(num_val[ord(ch)-ord('A')])
    else:
        b = stk.pop()
        a = stk.pop()
        if ch == '+':
            stk.append(a+b)
        elif ch == '-':
            stk.append(a-b)
        elif ch == '*':
            stk.append(a*b)
        else:
            stk.append(a/b)

print(f'{stk[0]:.2f}')
