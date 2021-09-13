def balls(n):
    # n = int(input())

    spell = ""

    while n > 0:
        if n % 2:
            spell = "A" + spell
            n -= 1
        else: 
            spell = "B" + spell
            n /= 2
    
    return spell

def ball_bit(n):
    spell = ["B"] * 60

    bit = format(n, "b")

    for b in bit: 
        

def checker(num_list):
    for num in num_list:
        n = 0
        spell = balls(num)
        
        for magic in spell:
            if magic == "A":
                n += 1
            else:
                n *= 2
        
        if n != num:
            print(num, spell)
            


if __name__  == "__main__":
    # n = int(input())
    # print(balls(n))

    list = list(range(1000001))
    checker(list)
    
