def solution(score):
    answer = []
    arr = list()
    arr2 = list()
    dic = {}
    for i in score:
        arr.append(sum(i))
        arr2.append(sum(i))
    arr.sort(reverse=True)
    dic[arr[0]] = 1
    con = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            con += 1
        else:
            con += 1
            dic[arr[i]] = con

    for j in arr2:
        for i, k in dic.items():
            if i == j:
                answer.append(k)
    return answer
