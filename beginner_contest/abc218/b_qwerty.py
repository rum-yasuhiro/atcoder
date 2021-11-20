def alphabet():
    origin = "abcdefghijklmnopqrstuvwxyz"
    output = ""

    p_list = list(map(int, input().split()))

    for p in p_list:
        output += origin[p - 1]

    return output


if __name__ == "__main__":
    print(alphabet())
