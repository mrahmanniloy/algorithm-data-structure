def gcd_faster(a, b):
    if b == 0:
        return a
    a_new = int(a % b)
    return gcd_faster(b, a_new)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd_faster(a, b))
