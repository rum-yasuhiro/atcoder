def name(): 
    n = int(input())

    fnames = []
    lnames = []
    for i in range(n):
        s, t = input().split()
        for fi, li in zip(fnames, lnames):
            if fi == s and li == t: 
                return "Yes"
        fnames.append(s)
        lnames.append(t)
    return "No"

if __name__ == "__main__":
    print(name())

