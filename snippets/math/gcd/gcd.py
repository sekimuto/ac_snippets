def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def gcd_multiple(nums: list):
    for i, b in enumerate(nums):
        if i == 0:
            a = b
            continue
            
        a = gcd(a, b)
    
    return a
