def inv_permutation():
    n = int(input())
    p = input().split()
    p = [int(i) for i in p]

    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = str(i + 1)

    return " ".join(q)


if __name__ == "__main__":
    print(inv_permutation())
