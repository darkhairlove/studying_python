rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
          "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
rate = 0
score = 0

for i in range(20):
    sj, sc, gr = input().split()

    if gr == 'P':
        continue
    rate += float(sc) * rating[gr]
    score += float(sc)

print(rate/score)
