button, rest = map(int, input().split())
result = 0
check = 0
text = list(input())
al_dic = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']}
for alpha in text:
    count = [number for number, chars in al_dic.items(
    ) if alpha in chars]
    if not count:
        result += button
        check = 0
    else:

        t = [c for c in range(len(al_dic[count[0]]))
             if alpha == al_dic[count[0]][c]]
        if check == count:
            result += rest + button*(t[0]+1)
        else:
            result += button*(t[0]+1)
        check = count
print(result)
