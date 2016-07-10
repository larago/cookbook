x = 126
y = 90

#Must fullfill condition x>=y 
def get_gcd(x, y):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    gcd = y
    print gcd

get_gcd(x, y)
