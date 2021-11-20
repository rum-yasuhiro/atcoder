def wether():
    n = int(input())
    s = input()
    if s[n - 1] == "o":
        return "Yes"
    else:
        return "No"


print(wether())
