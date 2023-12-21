def geometric_progression_nth_term(a, r, n):
    if n == 1:
        return a
    else:
        return r * geometric_progression_nth_term(a, r, n - 1)

def geometric_progression_sum(a, r, n):
    if n == 1:
        return a
    else:
        return a * (1 - r**n) / (1 - r)

def arithmetic_progression_nth_term(a, d, n):
    if n == 1:
        return a
    else:
        return a + (n - 1) * d

def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

