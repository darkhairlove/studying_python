num = int(input())
arr = input()

dic = {'000001': 'A', '000010': 'A', '000100': 'A', '001000': 'A', '010000': 'A', '000000': 'A', '100000': 'A',
       '011111': 'B', '001111': 'B', '000111': 'B', '101111': 'B', '001110': 'B', '001011': 'B', '001101': 'B',
       '010011': 'C', '010111': 'C', '011011': 'C', '110011': 'C', '000011': 'C', '010001': 'C', '010010': 'C',
       '011100': 'D', '001100': 'D', '010100': 'D', '011000': 'D', '111100': 'D', '011110': 'D', '011101': 'D',
       '100110': 'E', '000110': 'E', '100010': 'E', '100100': 'E', '110110': 'E', '101110': 'E', '100111': 'E',
       '101001': 'F', '001001': 'F', '100001': 'F', '101000': 'F', '111001': 'F', '101101': 'F', '101011': 'F',
       '110101': 'G', '010101': 'G', '100101': 'G', '110001': 'G', '110100': 'G', '111101': 'G', '110111': 'G',
       '111010': 'H', '011010': 'H', '101010': 'H', '110010': 'H', '111000': 'H', '111110': 'H', '111011': 'H'
       }
a2 = list()
sol = list()
j = 1

for i in range(len(arr)):
    if j < 6:
        a2.append(arr[i])
        j += 1
    elif j == 6:
        a2.append(arr[i])
        a2 = "".join(a2)
        if a2 in dic.keys():
            sol.append(dic.get(a2))
        else:
            sol.append('0')
        a2 = list()
        j = 1
k = 0
for i in sol:
    if i == '0':
        print(sol.index(i)+1)
        k += 1
        break
if k == 0:
    sol = "".join(sol)
    print(sol)
