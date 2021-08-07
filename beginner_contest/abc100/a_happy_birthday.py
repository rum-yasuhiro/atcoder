def pancake():
    a, b = map(int, input().split())
    if a <= 8 and b <= 8:
        return "Yay!"
    return ":("


if __name__ == "__main__":
    print(pancake())
