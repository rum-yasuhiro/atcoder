def digit_mod():
    n = input()

    s = 0
    for digit in n:
        s += int(digit)

    if int(n) % s == 0:
        return "Yes"
    return "No"


if __name__ == "__main__":
    print(digit_mod())
