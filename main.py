# 1

def power(a, b):
    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)
        
