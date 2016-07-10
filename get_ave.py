score = [40, 13, 89, 52, -1]

def get_ave(score):
    count = 0
    total = 0
    i = 0
    while score[i] != -1:
        count = count + 1
        total = score[i] + total
        i = i + 1
    ave = float(total) / count
    print ave

get_ave(score)