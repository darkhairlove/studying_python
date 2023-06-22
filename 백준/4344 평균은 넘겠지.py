import sys
input = sys.stdin.readline


def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)


T = int(input())

for _ in range(T):
    tmp = list(map(int, input().split()))
    people = tmp[0]
    scores = tmp[1:]

    avg = sum(scores) / people

    isOver = 0
    for score in scores:
        if score > avg:
            isOver += 1

    result = isOver / people * 100
    print(f'{roundTraditional(result, 3):.3f}%')
