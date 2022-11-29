num = int(input())
arr2 = input()
a = arr2.count('A')
b = arr2.count('B')
if a < b:
    print('B')
elif a > b:
    print('A')
else:
    print('Tie')
