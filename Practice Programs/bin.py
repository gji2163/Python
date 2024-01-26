def binary(n):
    n = list(n)
    return n.count('0') + n.count('1') == len(n)
