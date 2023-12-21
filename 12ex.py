def geomet_progres(n, b, g):
    return geomet_progres(n - 1, b, g) * g if n > 1 else b


def sum_geomet_progres(n, b, g):
    return sum_geomet_progres(n - 1, b, g) + b * g ** (n - 1) if n > 1 else b


def alg_progres(n, a, k):
    return alg_progres(n - 1, a, k) + k if n > 1 else a


def bin_x(a):
    return bin_x(a // 2) + [a % 2] if a else []


def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return a // gcd(a, b) * b


try:
    print(geomet_progres(3, 2, 2))
    print(sum_geomet_progres(3, 2, 2))
    print(alg_progres(3, 2, 2))
    print(bin_x(9))
    print(lcm(28, 56))
except ValueError:
    print("ERROR")
