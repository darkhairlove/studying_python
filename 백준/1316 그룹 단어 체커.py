num = int(input())
arr = num
for i in range(num):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            arr -= 1
            break
print(arr)
