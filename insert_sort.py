data = [77, 19, 80, 79, 20, 11]

def insert_sort(data):
    i = 1
    while i < len(data):
        k = 0
        while k < i:
            if data[k] > data[i]:
                break
            k += 1
        w = data[i]
        data[k+1:i+1] = data[k:i]
        data[k] = w
        i += 1
    print data
    

insert_sort(data)