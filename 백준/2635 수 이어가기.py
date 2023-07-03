num = int(input())

max_arr = []

for i in range(num+1):

    m_arr = [num]
    m_arr.append(i)
    indx = 1
    while 1:
        next_m = (m_arr[indx-1] - m_arr[indx])
        if next_m < 0:
            break
        m_arr.append(next_m)
        indx += 1
    if len(max_arr) < len(m_arr):
        max_arr = m_arr
print(len(max_arr))

print(*max_arr)
