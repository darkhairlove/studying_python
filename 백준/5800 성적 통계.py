num = int(input())
for i in range(num):
    arr = list(map(int, input().split()))
    arr.pop(0)
    print('Class ' + str(i+1))
    arr = sorted(arr)
    a = []
    for i in range(1, len(arr)):
        a.append(arr[i]-arr[i-1])

    print('Max ' + str(max(arr)) + ', ' + 'Min '+str(min(arr)) + ', ' +
          'Largest gap ' + str(max(a)))
