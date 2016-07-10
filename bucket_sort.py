bucket = [0 for i in range(10)]
data = [8, 2, 1, 5, 9, 7]

def bucket_sort(data):
    i = 0
    n = len(data)
    result = []
    while i < n:
        value = data[i]
        bucket[value] = bucket[value] + 1
        i += 1
    for index , item in enumerate(bucket):
        if item != 0:
            result.append(index)
    print result

bucket_sort(data)