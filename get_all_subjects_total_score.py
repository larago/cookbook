TEN = [
        [40, 70, 85],
        [60, 90, 70],
        [95, 100, 90],
        [72, 55, 65],
        [85, 50, 80]
      ]

def get_total_score(N):
    i = 0
    n = len(TEN)
    while i < n:
        N[i].append(0)
        j = 0
        while j < 3:
            N[i][3] = N[i][3] + N[i][j]
            j = j + 1
        i = i + 1
    print N

get_total_score(TEN)
