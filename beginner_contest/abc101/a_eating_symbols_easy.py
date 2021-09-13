def eat_symbol():
    symbols = input()

    output = 0
    for symbol in symbols:
        if symbol == "+":
            output += 1
        else:
            output -= 1

    return output


if __name__ == "__main__":
    print(eat_symbol())
