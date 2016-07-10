score = [40, 13, 89, 52, 7]

def get_rank(N):
    n = len(score)
    rank = [1 for i in range(n)]
    i = 0
    while i < n:
        j = 0
        while  j < n:
            if N[i] < N[j]:
                rank[i] = rank[i] + 1
            j = j + 1
        i = i + 1
    print rank

get_rank(score) 
