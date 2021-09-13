def sign():
    x, y = map(int, input().split("."))

    if y >= 0 and y <= 2: 
        print(str(x) + "-")
    elif y >= 3 and y <= 6: 
        print(str(x))
    elif y >= 7 and y <= 9: 
        print(str(x) + "+")
    
if __name__ == "__main__": 
    sign()