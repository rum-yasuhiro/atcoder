# make empty list
# loop 4 times
# input Si and if Si is not in list, them append
# if len(list) == 4, return Yes, else No


def c_hit():
    l = []
    for _ in range(4):
        s = input()
        if s in l:
            return "No"
        l.append(s)

    return "Yes"


if __name__ == "__main__":
    ans = c_hit()
    print(ans)
