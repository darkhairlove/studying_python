score_sum = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    score_sum += score
print(score_sum//5)
