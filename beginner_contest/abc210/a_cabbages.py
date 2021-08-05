def cabbages():
    # input each variables
    # compare "n" and "a" to divide each cases
    # if a > n, then tot_sum = n*x
    # else, then tot_sum = a*x + (n-a)*y

    n, a, x, y = map(int, input().split())

    if a >= n:
        tot_sum = n * x
    else:
        tot_sum = a * x + (n - a) * y

    return tot_sum


if __name__ == "__main__":
    ans = cabbages()
    print(ans)
