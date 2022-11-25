class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        arr1 = list()
        arr2 = list()
        sol = 0
        for i in range(len(z)):
            arr1.append(z[i])
            arr2.append(z[i])
        arr1.reverse()
        for i, j in zip(arr1, arr2):
            if i == j:
                sol += 1
            else:
                sol = 0
                break
        return sol
