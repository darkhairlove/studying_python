def recursion(s, l, r, c):
    if l >= r:
        c += 1
        print("1"+" "+str(c))
    elif s[l] != s[r]:
        c += 1
        print("0"+" "+str(c))
    else:
        c += 1
        return recursion(s, l+1, r-1, c)


def isPalindrome(s):
    c = 0
    return recursion(s, 0, len(s)-1, c)


num = int(input())
for _ in range(num):
    str_ = input()
    isPalindrome(str_)
