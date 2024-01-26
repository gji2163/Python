def max1(*num):
    return max(*num)
def max2(*num):
    m=0
    for i in num:
        if i>m:
            m=i
    return m
