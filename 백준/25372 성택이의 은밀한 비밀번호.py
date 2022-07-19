num = int(input())

for i in range(num):
    arr = list(input())
    if 6 <= len(arr) <= 9:
        print("yes")
    else:
        print("no")
