def sum1(*num):
    return sum(num)

def sum2(*num):
    s=0
    for i in num:
        s+= i
    return s
