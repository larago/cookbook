#Warning: these codes hasn't been completed yet

import math
data = [8, 2, 4, 12, 1, 9, 6, 3]

def merge_sort(data):
    if len(data)%2 == 0:
        num = len(data)
        j = 0
        while num != 2:
            num = num / 2
            j += 1
        group_num = len(data) / j      +
        k = 0
        i = 0
        while k < j: 
            group = [data[i], data[i+2^k]] * group_num
            k += 1
            i += 2^k
        print group

merge_sort(data)