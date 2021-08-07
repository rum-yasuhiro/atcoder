def snow():
    a, b = map(int, input().split())

    n = b - a

    # slower
    # # 1 + 2 + 3 + ... + n = n*(n+1)/2
    # b_tot = int(n * (n + 1) / 2)
    # return b_tot - b

    # faster
    b_tot = 0
    for i in range(1, n + 1):
        b_tot += i
    return b_tot - b


if __name__ == "__main__":
    print(snow())
