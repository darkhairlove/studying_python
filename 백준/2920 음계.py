arr = []
i = 1

for i in range(8):
    arr.append(int(input()))

for i in arr:
    if i+1 > i:
        print('ascending')
