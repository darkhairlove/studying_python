a1 = input()
a2 = input()

con = 0
arr = list(a1.replace(a2, '0'))
for i in arr:
    if i == '0':
        con += 1
print(con)
