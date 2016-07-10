data = [19, 80, 77, 11, 54]

def bubble_sort(data):
    j=0
    while j < len(data):
        i = 0
        while i < len(data)-1:
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
            i += 1
        j += 1
    print data

bubble_sort(data)
