num = int(input())
arr = []
for i in range(num):
    arr.append(input())
k = 0
s = 0
for i in range(len(arr)):
    k_ = []
    for j in range(len(arr[i])):
        if arr[i][j] == '.':
            k_.append(arr[i][j])
        elif arr[i][j] == 'X':
            if len(k_)>= 2:
                k += 1
                k_ = []
            else:
                k_ = []
    if k_.count('.') >=2:
        k+=1
for i in range(len(arr)):
    s_ = []
    for j in range(len(arr[i])):
        if arr[j][i] == '.':
            s_.append(arr[j][i])
        elif arr[j][i] == 'X':
            if len(s_)>= 2:
                s += 1
                s_ = []
            else:
                s_ = []
    if s_.count('.') >=2:
        s+=1        

print(k, s)
    