def quiz():
    pool = ["ABC", "ARC", "AGC", "AHC"]
    for _ in range(3):
        s = input()
        pool.remove(s)

    return pool[0]


if __name__ == "__main__":
    print(quiz())
