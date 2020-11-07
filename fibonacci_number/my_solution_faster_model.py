def fibNum(n):
    if n <= 1:
        return n
    arr = []
    while len(arr) < n + 1:
        arr.append(0)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibNum(input_n))
