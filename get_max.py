score = [40, 13, 89, 52, 7]

def get_max(N):
    max_num = -1
    i = 0
    n = len(N)
    while i < n:
        if N[i] > max_num:
            max_num = score[i]
        i = i + 1
    print max_num

get_max(score)