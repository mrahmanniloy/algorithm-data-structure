def gcd_faster(a, b):
    if b == 0:
        return int(a)
    a_new = int(a % b)
    return gcd_faster(b, a_new)


def lcm_faster(a, b):
    m = gcd_faster(a, b)
    return int((a / m) * b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_faster(a, b))
