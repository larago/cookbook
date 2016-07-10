score = [40, 13, 89, 52, 7]

def get_min(N):
    min_num = 101
    i = 0
    n = len(N)
    while i < n:
        if N[i] < min_num:
            min_num = N[i]
        i = i + 1
    print min_num

get_min(score)