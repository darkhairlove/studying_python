num = int(input())
arr = list(map(int,input().split()))
b_num = int(input())

arr.append(0)
arr.sort()

a=0
for i in range(len(arr)-1):
    if arr[i] == b_num or arr[i+1] == b_num:
        a = 0
        break
    elif arr[i] < b_num and arr[i+1] > b_num:
        a = (b_num- arr[i])*(arr[i+1] - b_num)  - 1
        break
print(a)

           