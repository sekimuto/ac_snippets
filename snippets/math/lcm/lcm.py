def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_multiple(nums: list):
    for i, b in enumerate(nums):
        if i == 0:
            a = b
            continue

        a = lcm(a, b)
    
    return a
