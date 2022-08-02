
def is_prime_number(x):
    if x == 1:
        return False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


def solution(nums):
    a = len(nums)
    answer = 0
    i = 0
    while i < a-2:
        j = i+1
        while j < a-1:
            k = j+1
            while k < a:
                if is_prime_number(nums[i]+nums[j]+nums[k]):
                    answer += 1
                k += 1
            j += 1
        i += 1
    return answer
