def dict_order():
    s, t = input().split()

    l = [s, t]
    l.sort()
    if l[0] == s:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(dict_order())
