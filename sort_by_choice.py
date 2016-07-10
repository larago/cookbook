data = [35, 80, 21, 54, 11, 45, 92, 39]

def sort_by_choice(data):
    i = 0
    n = len(data)
    min_num = 9999
    result = []
    while i < n:
        min_num = min(data)
        data.remove(min_num)
        result.append(min_num)
        i += 1
    print result

sort_by_choice(data)