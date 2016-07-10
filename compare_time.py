time1 = 6 * 3600 + 32 * 60 + 12
time2 = 9 * 3600 + 10 * 60 + 52

def compare_time(time1, time2):
    dis = abs(time1-time2)
    h = dis/3600
    r = dis%3600
    m = r/60
    s = r%60
    print '%sh%sm%ss' % (h, m, s)

compare_time(time1, time2)